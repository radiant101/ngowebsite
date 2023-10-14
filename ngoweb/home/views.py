from django.shortcuts import render,HttpResponse

# Create your views here from here you display the http respons tto the site.
def home (request):
    #return HttpResponse("THIS IS MY HOMEPAGE(/)")
    return render(request, 'home.html')

def about (request):
    #return HttpResponse("THIS IS MY  about PAGE(/about)")
     return render(request, 'about.html')
def ngos (request):
   # return HttpResponse("THIS IS MY ngos PAGE(/)")
    return render(request, 'ngos.html')
def contact (request):
   # return HttpResponse("THIS IS MY contact PAGE(/)")
    return render(request, 'contact.html')