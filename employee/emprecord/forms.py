# forms.py
from django import forms
from .models import Employee, Factory, Stream

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'employee_id', 'date_of_birth',
                  'gender', 'email', 'phone_number', 'address']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class FactoryForm(forms.ModelForm):
    class Meta:
        model = Factory
        fields = ['factory_code', 'factory_name', 'location']

class StreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields = ['employee', 'factory', 'stream_date', 'status']
