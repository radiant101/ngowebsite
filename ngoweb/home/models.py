from django.db import models
import os
import datetime
import datetime
from geopy.geocoders import Nominatim 
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
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('static/', filename)

class Item(models.Model):
    email = models.CharField(max_length=100)
    textarea = models.TextField(max_length=5000, null=True)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    is_ngo = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.address:
            # Use Nominatim for geocoding
            geolocator = Nominatim(user_agent="YourAppName/1.0")
            location = geolocator.geocode(self.address)

            if location:
                self.latitude, self.longitude = location.latitude, location.longitude
                print(f"Latitude: {self.latitude}, Longitude: {self.longitude}")
            else:
                print(f"Geocoding failed for address: {self.address}")

        super().save(*args, **kwargs)

