from django import forms
from django.contrib.auth.models import User
from . import models
from .models import Vehicle, Request, Garage, Customer

class VehicleRegistrationForm(forms.ModelForm):
    vehicle_type = forms.ChoiceField(
        choices=Vehicle.VEHICLE_TYPE_CHOICES,  # Ensure this matches the choices in the model
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Vehicle
        fields = ['model', 'make', 'year', 'registration_number', 'status', 'last_service_date', 'next_service_due', 'vehicle_type']


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class CustomerForm(forms.ModelForm):
    customer = forms.ChoiceField(
        choices=Customer.CUSTOMER_CHOICES,  # Updated to match the model
        widget=forms.Select(attrs={'class': 'form-control'})  # Add Bootstrap styling
    )

    class Meta:
        model = Customer
        fields = ['customer', 'address', 'mobile', 'profile_pic']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'})
        }


class MechanicUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class MechanicForm(forms.ModelForm):
    class Meta:
        model=models.Mechanic
        fields=['address','mobile','profile_pic','skill']

class MechanicSalaryForm(forms.Form):
    salary=forms.IntegerField();


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['category', 'vehicle_no', 'vehicle_name', 'vehicle_model', 'vehicle_brand', 'problem_description', 'department', 'image']
        widgets = {
            'problem_description': forms.Textarea(attrs={'rows': 3, 'cols': 30}),
        }

class AdminRequestForm(forms.Form):
    #to_field_name value will be stored when form is submitted.....__str__ method of customer model will be shown there in html
    customer=forms.ModelChoiceField(queryset=models.Customer.objects.all(),empty_label="Customer Name",to_field_name='id')
    mechanic=forms.ModelChoiceField(queryset=models.Mechanic.objects.all(),empty_label="Mechanic Name",to_field_name='id')
    cost=forms.IntegerField()

class AdminApproveRequestForm(forms.Form):
    mechanic=forms.ModelChoiceField(queryset=models.Mechanic.objects.all(),empty_label="Mechanic Name",to_field_name='id')
    cost=forms.IntegerField()
    stat=(('Pending','Pending'),('Approved','Approved'),('Released','Released'))
    status=forms.ChoiceField( choices=stat)


class UpdateCostForm(forms.Form):
    cost=forms.IntegerField()

class MechanicUpdateStatusForm(forms.Form):
    stat=(('Approved','Approved'),('Repairing','Repairing'),('Repairing Done','Repairing Done'))
    status=forms.ChoiceField( choices=stat)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['by','message']
        widgets = {
        'message':forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }

#for Attendance related form
presence_choices=(('Present','Present'),('Absent','Absent'))
class AttendanceForm(forms.Form):
    present_status=forms.ChoiceField( choices=presence_choices)
    date=forms.DateField()

class AskDateForm(forms.Form):
    date=forms.DateField()


#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class GarageForm(forms.ModelForm):
    class Meta:
        model = Garage
        fields = ['name', 'location', 'status', 'mechanic']  # Specify the fields to include in the form