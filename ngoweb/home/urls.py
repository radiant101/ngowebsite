from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('ngos',views.ngos, name='ngos'),
    path('add/', views.addProduct, name='add_Product'),
    path('report/',views.addProduct,name='report'),
    path('contact',views.contact_form, name='contact'),
    path('volunteer',views.volunteer,name='volunteer')
    

]
