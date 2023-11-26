from django.shortcuts import render,HttpResponse
from home.models import contact
from home.models import Item

# Create your views here from here you display the http respons tto the site.
def home (request):
    return render(request, 'home.html')
def about (request):
    #return HttpResponse("THIS IS MY  about PAGE(/about)")
     return render(request, 'about.html')
def report (request):
     return render(request, 'report.html')


from django.shortcuts import render, redirect


def ngos (request):
   # return HttpResponse("THIS IS MY ngos PAGE(/)")
    return render(request, 'ngos.html')
def contact_form (request):
   if request.method=="POST":
       firstname = request.POST['firstname']
       lastname = request.POST['lastname']
       subject = request.POST['subject']
       inputCity = request.POST['inputCity']
       state=request.POST['state']
       #print(firstname, lastname, subject, inputcity,state )
       contact_instance=contact(firstname= firstname,lastname=lastname,subject=subject,inputcity=inputCity,state=state)
       contact_instance.save()
       print("the data has been written to the database")
   # return HttpResponse("THIS IS MY contact PAGE(/)")
   return render(request, 'contact.html')
#def addProduct(request):
   if request.method == "POST":
      prod=Item()
      prod.email= request.POST.get('emailaddress')
      prod.textarea= request.POST.get('description2')
      if len(request.FILES) !=0:
       prod.image= request.FILES['image']

      prod.save()
      return HttpResponse(request, "product added succesfullly")
   return render(request,'report.html')

def volunteer(request):
    return render(request,'volunteer.html')



#please adddd
# views.py
from django.shortcuts import render, HttpResponse
from geopy.geocoders import Nominatim
from .utils import calculate_distance, notify_nearby_ngos
from home.models import Item
from django.core.mail import EmailMessage
from .models import NGO
from geopy.distance import geodesic
from django.core.mail import send_mail
from home.models import contact

def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    return HttpResponse("Invalid Request")

def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

def send_notification_email(ngo_email, image_path=None):
    subject = 'Report'
    message = f'You have a new Report.'
    from_email = 'zoroackerman101@gmail.com'
    recipient_list = [ngo_email]

    email = EmailMessage(subject, message, from_email, recipient_list)
    if image_path:
        with open(image_path.image.path, 'rb') as image_file:
            email.attach('image.jpg', image_file.read(), 'image/jpeg')

    email.send()
    print(f"Email sent successfully to {ngo_email}")

def notify_nearby_ngos(user_location, user_address, ngos):
    user_lat, user_lon = user_location
    user_coord = (user_lat, user_lon)

    nearby_ngos = []

    for ngo in ngos:
        ngo_location = (ngo.latitude, ngo.longitude)
        distance = calculate_distance(user_coord, ngo_location)

        if distance is not None and distance < 3:
            nearby_ngos.append(ngo)
            send_notification_email(ngo.email)
            print(f"Notified NGO {ngo.name} ({ngo.email}) about the report.")

    return nearby_ngos



def addProduct(request):
    if request.method == "POST":
        prod = Item()
        prod.email = request.POST.get('emailaddress')
        prod.textarea = request.POST.get('description')
        prod.address = request.POST.get('address')

        geolocator = Nominatim(user_agent="YourAppName/1.0")
        
        # Geocode the address
        location = geolocator.geocode(prod.address)
        if location:
            prod.latitude, prod.longitude = location.latitude, location.longitude
        else:
            print(f"Geocoding failed for address: {prod.address}. No location found.")

        # Check if 'image' is in request.FILES
        if 'image' in request.FILES:
            prod.image = request.FILES['image']

        # Save the product without exception handling
        prod.save()

        # Notify nearby NGOs
        user_location = (prod.latitude, prod.longitude)
        user_address = prod.address
        ngos = NGO.objects.all()
        nearby_ngos = notify_nearby_ngos(user_location, user_address, ngos)

        for ngo in nearby_ngos:
            send_notification_email(ngo.email, prod)

        print('Product added successfully')

        # Return success response
        return HttpResponse("Product added successfully")

    # If the request method is not POST, render the 'add.html' template
    return render(request, 'add.html')

