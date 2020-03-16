from django.contrib import admin
from .models import getInvolved,Donate,app         #importing the product from our models.py

# Register your models here.
admin.site.register(getInvolved)
admin.site.register(Donate)
admin.site.register(app)