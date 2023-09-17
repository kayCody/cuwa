from rest_framework.serializers import ModelSerializer
from database.models import Customer, Agent

class AgentSerializer(ModelSerializer):
  class Meta:
    model = Agent
    fields = ['id','password','username', 'fullname', 'Position']

class CustomerSerializer(ModelSerializer):
  class Meta:
    model = Customer
    fields = '__all__'