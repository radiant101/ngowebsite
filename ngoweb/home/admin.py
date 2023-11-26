from django.contrib import admin
from home.models import contact, NGO,Item


# Register your models here.
admin.site.register(contact)
admin.site.register(NGO)
admin.site.register(Item)