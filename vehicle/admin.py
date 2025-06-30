from django.contrib import admin
from .models import Customer, Mechanic, Request, Attendance, Feedback, Garage

# Custom admin classes for enhanced management

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile', 'address')  # Columns to display in the list view
    search_fields = ('user__username', 'user__first_name', 'user__last_name')  # Searchable fields

class MechanicAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile', 'address', 'skill', 'salary', 'status')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'skill')
    list_filter = ('status',)  # Add filtering by status

class RequestAdmin(admin.ModelAdmin):
    list_display = ('vehicle_name', 'vehicle_no', 'category', 'problem_description', 'status', 'date', 'customer', 'mechanic', 'cost')
    search_fields = ('vehicle_name', 'vehicle_model', 'vehicle_brand', 'customer__user__username', 'mechanic__user__username')
    list_filter = ('status', 'category', 'date')  # Add filtering options

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('mechanic', 'date', 'present_status')
    search_fields = ('mechanic__user__username',)
    list_filter = ('present_status', 'date')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('by', 'date', 'message')
    search_fields = ('by', 'message')
    list_filter = ('date',)

class GarageAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'mechanic', 'status')
    search_fields = ('name', 'location')  # Optional: add search functionality
    list_filter = ('status',)  # Optional: filter by status (pending, approved, etc.)

# Registering models with the custom admin classes
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Mechanic, MechanicAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Garage, GarageAdmin)
