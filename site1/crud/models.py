from django.db import models
from django.contrib.auth.models  import User
# Create your models here.
class Employee(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    job=models.CharField(max_length=30)
    
    def __str__(self):
        return self.firstname
    
