from django.db import models

# Create your models here.


class contact(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    subject=models.TextField()
    inputcity=models.CharField(max_length=50)
    state=models.CharField(max_length=80)
