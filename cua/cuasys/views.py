from django.shortcuts import render
from database.models import Customer, Agent

# Create your views here.
def login(request):
  return render(request, 'auth/login.html')


def dashboard(request):
  customers = Customer.objects.all()
  context={
      'customers': customers,
  }
    
  return render(request, 'pages/home.html', context)
def customer(request, idNo):
  customer = Customer.objects.get(idNo = idNo)
  context={
      'customer': customer,
  }
    
  return render(request, 'pages/customer.html', context)
def notification(request):
  return render(request, 'pages/notification.html')
