from django.db import models

# Create your models here.

class Person(models.Model):
    Name = models.CharField(max_length=100)
    PhoneNo = models.CharField(max_length=11)
    Email = models.EmailField(max_length=100)
    Address = models.CharField(max_length=150)
    DateOfBirth = models.DateField()
    Gender = models.CharField(max_length=100)
    LockerAssignment = models.CharField(max_length=100)


class RegisteredUser(models.Model):
    PersonId = models.ForeignKey(Person,on_delete=models.CASCADE)
    FitnessGoals=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='images/')



