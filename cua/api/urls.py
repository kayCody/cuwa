from django.urls import path
from . import views
urlpatterns = [
  path('agents/',views.agents),
  path('customers/',views.customers),
  path('customer/<int:id>', views.CustomerDetails),
]