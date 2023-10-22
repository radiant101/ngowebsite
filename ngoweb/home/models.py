from django.db import models

# Create your models here.

# create model for contacts
class contact(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    subject=models.TextField()
    inputcity=models.CharField(max_length=50)
    state=models.CharField(max_length=80)
 
class NGO(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # Add more fields as needed

class Report(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='reports/', blank=True, null=True)
    location = models.CharField(max_length=100)
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)
    # Add more fields as needed