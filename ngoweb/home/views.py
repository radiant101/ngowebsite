from django.shortcuts import render,HttpResponse
from home.models import contact
# Create your views here from here you display the http respons tto the site.
def home (request):
    #return HttpResponse("THIS IS MY HOMEPAGE(/)")
    return render(request, 'home.html')

def about (request):
    #return HttpResponse("THIS IS MY  about PAGE(/about)")
     return render(request, 'about.html')
def report (request):
     return render(request, 'report.html')

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