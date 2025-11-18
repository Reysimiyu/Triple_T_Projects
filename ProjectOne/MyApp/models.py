from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Student(models.Model):
    firstName=models.CharField(max_length=100)
    secondName=models.CharField(max_length=100)
    age=models.IntegerField()
    create_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName

class addStudent(models.Model):
    first_name=models.CharField(max_length=100,blank=False,null=False)
    last_name=models.CharField(max_length=100,blank=False,null=False)
    std_email=models.EmailField()
    std_regNo=models.CharField(max_length=100,blank=False,null=False)

    def __str__(self):
        return self.first_name
    
    # def clean(self):
    #     if not self.first_name or not self.last_name or not self.std_email or not self.std_regNo:
    #         raise ValidationError('All fields are required')