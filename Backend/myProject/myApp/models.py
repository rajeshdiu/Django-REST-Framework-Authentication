from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    
    
    USER = [
        ('Admin','Admin'),
        ('Employee','Employee'),
    ]
    
    User_Type = models.CharField(choices=USER,max_length=100,null=True)
    
    
class DepartmentModel(models.Model):
    Created_By = models.ForeignKey(CustomUser,on_delete=models.CASCADE,max_length=100,null=True)
    Department_Name = models.CharField(max_length=100,null=True)
    Description = models.TextField(null=True)


class EmployeeModel(models.Model):
    
    Created_By = models.ForeignKey(CustomUser,on_delete=models.CASCADE,max_length=100,null=True)
    Department = models.ForeignKey(DepartmentModel,on_delete=models.CASCADE,max_length=100,null=True)
    Full_Name = models.CharField(max_length=100,null=True)
    Phone = models.CharField(max_length=100,null=True)
    Position = models.CharField(max_length=100,null=True)
    Date_of_Joining = models.DateField(auto_now_add=True,null=True)
    Profile_Picture = models.ImageField(upload_to="Media/Employee_Picture",null=True)
    
class LeaveModel(models.Model):
    
    LEAVE =[
        ('SICK_LEAVE','SICK_LEAVE'),
        ('CASUAL_LEAVE','CASUAL_LEAVE'),
        ('ANNUAL_LEAVE','ANNUAL_LEAVE'),
    ]
    
    STATUS =[
        ('Pending','Pending'),
        ('Approved','Approved'),
        ('Rejected','Rejected'),
    ]
    
    Employee = models.ForeignKey(EmployeeModel,on_delete=models.CASCADE,null=True)
    Leave_Type = models.CharField(choices=LEAVE,null=True)
    From_Date = models.DateField(null=True)
    To_Date = models.DateField(null=True)
    Reason = models.TextField(null=True)
    Leave_Status = models.CharField(choices=STATUS,default="Pending",null=True)
    
