from django.db import models

# Create your models here.
class Employee(models.Model):
    Emp_ID = models.IntegerField()
    Emp_Name = models.CharField(max_length=64)
    Experience = models.IntegerField()
    Salary = models.IntegerField()
    Address = models.CharField(max_length=256)
    Tech_Skills = models.CharField(max_length=256)