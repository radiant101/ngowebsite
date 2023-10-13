from django.shortcuts import render,HttpResponse

# Create your views here.
def home (request):
    #return HttpResponse("THIS IS MY HOMEPAGE(/)")
    return render(request, 'home.html')

def about (request):
    return HttpResponse("THIS IS MY  about PAGE(/about)")

def ngos (request):
    return HttpResponse("THIS IS MY ngos PAGE(/)")

def contact (request):
    return HttpResponse("THIS IS MY contact PAGE(/)")
