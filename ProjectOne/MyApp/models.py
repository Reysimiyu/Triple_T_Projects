from django.db import models

# Create your models here.
class Student(models.Model):
    firstName=models.CharField(max_length=100)
    secondName=models.CharField(max_length=100)
    age=models.IntegerField()
    create_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName
