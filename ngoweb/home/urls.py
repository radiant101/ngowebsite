from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('ngos',views.ngos, name='ngos'),
    path('report/',views.addProduct,name='report'),
    path('contact',views.contact_form, name='contact'),
    
    

]
