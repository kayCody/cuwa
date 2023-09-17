from django.contrib import admin
from .models import Customer, Agent

# Register your models here.
admin.site.register(Customer)
admin.site.register(Agent)