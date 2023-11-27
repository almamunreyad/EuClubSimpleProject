from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=150)
    std_id = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    message = models.TextField()
    

class SignUp(models.Model):
    image = models.FileField(upload_to='media/signup/', null=True)
    name = models.CharField(max_length=150, null=True)
    std_id = models.CharField(max_length=50, null=True)
    club = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=80, null=True)
    password = models.CharField(max_length=50, null=True)
    
class Member(models.Model):
    member_image = models.ImageField(upload_to='media/')
    mem_name = models.CharField(max_length=150)
    std_id = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    join_date = models.DateField(null=True)
    