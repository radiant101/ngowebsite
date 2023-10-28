from django.db import models
import os
import datetime
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

def filepath(request,filename):
    old_filename=filename
    timeNow= datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename="%s%s" % ( timeNow ,old_filename)
    return os.path.join('static/', filename)

class Item(models.Model):
    email = models.CharField(max_length=100)
    textarea = models.TextField(max_length=5000, null=True)
    image = models.ImageField(upload_to=filepath, null=True,blank=True)
