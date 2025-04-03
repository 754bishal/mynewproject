from django.db import models

# CREATE TABLE EMPLOYEES (first name varchar(60))
class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    hire_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_id})"


class Factory(models.Model):
    factory_code = models.CharField(max_length=10, unique=True)
    factory_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.factory_code} - {self.factory_name}"


class Stream(models.Model):
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
        ('P', 'Pending'),
    )
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    
    class Meta:
        unique_together = ('employee', 'factory')
    
    def __str__(self):
        return f"{self.employee.first_name} assigned to {self.factory.factory_name} ({self.status})"
