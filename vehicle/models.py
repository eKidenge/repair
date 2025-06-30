from django.db import models
from django import forms  # Add this import
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)

    # Define the department choices
    CUSTOMER_CHOICES = [
        ('Health and Emergency Services', 'Health and Emergency Services'),
        ('Education, ICT, e-Government & Public Communication', 'Education, ICT, e-Government & Public Communication'),
        ('Agriculture, Livestock, Fisheries & Veterinary Services', 'Agriculture, Livestock, Fisheries & Veterinary Services'),
        ('Infrastructure', 'Infrastructure'),
        ('Lands, Housing & Physical Planning', 'Lands, Housing & Physical Planning'),
        ('Trade, Cooperatives, Tourism, Culture', 'Trade, Cooperatives, Tourism, Culture'),
        ('Environment, Energy, Climate Change & Natural Resources', 'Environment, Energy, Climate Change & Natural Resources'),
        ('Youths, Sports, Gender, Social Services & Inclusivity', 'Youths, Sports, Gender, Social Services & Inclusivity'),
        ('Office of the County Secretary', 'Office of the County Secretary'),
        ('Department of Public Service, Devolution', 'Department of Public Service, Devolution'),
        ('Finance and Economic Planning', 'Finance and Economic Planning'),
    ]

    customer = models.CharField(max_length=100, choices=CUSTOMER_CHOICES, default='Finance and Economic Planning')

    @property
    def get_name(self):
        """Returns the full name of the customer."""
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_instance(self):
        """Returns the instance of the model."""
        return self

    def __str__(self):
        """String representation of the customer."""
        return self.user.first_name


class Vehicle(models.Model):
    STATUS_CHOICES = (
        ('Awaiting Inspection', 'Awaiting Inspection'),
        ('Approved for Repair', 'Approved for Repair'),
        ('Operational', 'Operational'),
        # Add more statuses as needed
    )

    VEHICLE_TYPE_CHOICES = (
        ('Car', 'Car'),
        ('Truck', 'Truck'),
        ('Motorbike', 'Motorbike'),
        ('Van', 'Van'),
        # Add more vehicle types as needed
    )

    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.IntegerField()
    registration_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    last_service_date = models.DateField()
    next_service_due = models.DateField()
    vehicle_type = models.CharField(max_length=50, choices=VEHICLE_TYPE_CHOICES, default='Car')  # Default value added here
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Add this line to associate a customer with a vehicle

    def __str__(self):
        return f'{self.model} - {self.registration_number}'

class Mechanic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/MechanicProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    skill = models.CharField(max_length=500, null=True)
    salary = models.PositiveIntegerField(null=True)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name


class Request(models.Model):
    department = (
        ('Health and Emergency Services', 'Health and Emergency Services'),
        ('Education, ICT, e-Government & Public Communication', 'Education ICT, e-Government & Public Communication'),
        ('Agriculture, Livestock, Fisheries & Veterinary Services', 'Agriculture, Livestock, Fisheries & Veterinary Services'),
        ('Infrastructure', 'Infrastructure'),
        ('Lands, Housing & Physical Planning', 'Lands, Housing & Physical Planning'),
        ('Trade, Cooperatives, Tourism, Culture', 'Trade, Cooperatives, Tourism, Culture'),
        ('Environment, Energy, Climate Change & Natural Resources', 'Environment, Energy, Climate Change & Natural Resources'),
        ('Youths, Sports, Gender, Social Services & Inclusivity', 'Youths, Sports, Gender, Social Services & Inclusivity'),
        ('Office of the County Secretary', 'Office of the County Secretary'),
        ('Department of Public Service, Devolution', 'Department of Public Service, Devolution'),
        ('Finance and Economic Planning', 'Finance and Economic Planning'),
    )

    cat = (
        ('Track', 'Track'),
        ('Heavy Machinery', 'Heavy Machinery'),
        ('Prime Mover', 'Prime Mover'),
        ('two wheeler with gear', 'two wheeler with gear'),
        ('two wheeler without gear', 'two wheeler without gear'),
        ('three wheeler', 'three wheeler'),
        ('four wheeler', 'four wheeler'),
    )
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)  # Add this line
    category = models.CharField(max_length=50, choices=cat)

    vehicle_no = models.CharField(max_length=50, null=False)  # Changed from PositiveIntegerField to CharField
    vehicle_name = models.CharField(max_length=40, null=False)
    vehicle_model = models.CharField(max_length=40, null=False)
    vehicle_brand = models.CharField(max_length=40, null=False)

    problem_description = models.CharField(max_length=500, null=False)
    date = models.DateField(auto_now=True)
    cost = models.PositiveIntegerField(null=True)

    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    mechanic = models.ForeignKey('Mechanic', on_delete=models.CASCADE, null=True)

    stat = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Repairing', 'Repairing'),
        ('Repairing Done', 'Repairing Done'),
        ('Released', 'Released'),
    )
    status = models.CharField(max_length=50, choices=stat, default='Pending', null=True)

    department = models.CharField(max_length=100, choices=department)

    def __str__(self):
        return self.problem_description


class Attendance(models.Model):
    mechanic = models.ForeignKey('Mechanic', on_delete=models.CASCADE, null=True)
    date = models.DateField()
    present_status = models.CharField(max_length=10)


class Feedback(models.Model):
    date = models.DateField(auto_now=True)
    by = models.CharField(max_length=40)
    message = models.CharField(max_length=500)


class Report(models.Model):
    # Foreign key to Request to create reports for each request
    request = models.ForeignKey('Request', on_delete=models.CASCADE)
    
    # Additional fields for storing report data (if necessary)
    customer_name = models.CharField(max_length=100)
    mechanic_name = models.CharField(max_length=100)
    vehicle_details = models.CharField(max_length=500)
    problem_description = models.CharField(max_length=500)
    status = models.CharField(max_length=50)

    # Method to populate the report with details from the related Request
    def generate_report(self):
        # Fetching related customer and mechanic names
        self.customer_name = self.request.customer.get_name if self.request.customer else 'N/A'
        self.mechanic_name = self.request.mechanic.get_name if self.request.mechanic else 'N/A'
        
        # Fetching vehicle details
        self.vehicle_details = f"{self.request.vehicle_name} - {self.request.vehicle_model} ({self.request.vehicle_brand})"
        
        # Set other details
        self.problem_description = self.request.problem_description
        self.status = self.request.status
        
        self.save()

    def __str__(self):
        return f"Report for {self.customer_name} - {self.problem_description}"

class Garage(models.Model):
    # Fields for the Garage model
    name = models.CharField(max_length=100)  # Name of the garage
    location = models.CharField(max_length=255)  # Location of the garage
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])  # Garage status
    mechanic = models.CharField(max_length=100)  # Name of the mechanic in charge

    def __str__(self):
        return self.name

