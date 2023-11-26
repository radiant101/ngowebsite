from geopy.distance import geodesic
from django.core.mail import send_mail
import requests


def calculate_distance(coord1,coord2):
        return geodesic(coord1, coord2).kilometers
  

def send_notification_email(ngo_email):
    
        subject = 'You have a new notification'
        message = f'You have a new Report.'
        from_email = 'zoroackerman101@gmail.com'
        recipient_list = [ngo_email]

        send_mail(subject, message, from_email, recipient_list)
    

def notify_nearby_ngos(user_location,user_address,ngos):
    user_lat,user_lon =user_location
    user_coord =(user_lat,user_lon)
    
    nearby_ngos = []

    for ngo in ngos:
        ngo_location=(ngo.latitude,ngo.longitude)

        distance =calculate_distance(user_coord, ngo_location)
        if distance is not None and distance < 8:  #Adjust the radius
            nearby_ngos.append(ngo)
            #Notify the NGO (via email)
            send_notification_email(ngo.email)

    return nearby_ngos
