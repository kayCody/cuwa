from django.shortcuts import render, HttpResponse
from database.models import Customer, Agent
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import AgentSerializer, CustomerSerializer
from django.db.models import Q

# Create your views here.
@api_view(['GET', 'POST'])
def agents(request):
  agents = Agent.objects.all()
  if request.method=='GET':
    serializer = AgentSerializer(agents, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def customers(request):
  query = request.GET.get('query')
  if query == None:
    query = ''
  customers = Customer.objects.filter(Q(idNo__icontains=query) | Q(name__icontains =query) | Q(accountNo__icontains=query))
  serializer= CustomerSerializer(customers, many = True)
  return Response(serializer.data)

def CustomerDetails(request, id):
  customers = Customer.objects.get(idNo = id)
  if request.method == 'GET':
    serializer = CustomerSerializer(customers, many=False)
    return Response(serializer.data)