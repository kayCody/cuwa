from django.db import models

OPTIONS=[
  ('Field Agent','Field Agent')
]
# Create your models here.


class Agent(models.Model):
  username = models.CharField(max_length=50, blank=True, null=True)
  password = models.CharField(max_length=100, blank=False, null=False, editable=False)
  fullname = models.CharField(max_length=100, blank=False, null=False)
  Position = models.CharField(max_length=50, blank=True, null=True, choices=OPTIONS)
  class Meta:
        ordering = ['id']
  def __str__(self):
    return self.username
  
  def save(self, *args, **kwargs):
      passwd=self.username + str(self.id) + '@'
      self.password=passwd
      super().save(self, *args, **kwargs)
  


class Customer(models.Model):
  idNo = models.IntegerField(blank=True, null=False, primary_key=True)
  accountNo = models.IntegerField(blank=True, null=True )
  name = models.CharField(max_length=150, blank=False, null=False)
  branch = models.CharField(max_length=150, blank=False, null=False)
  address = models.CharField(max_length=150, blank=False, null=False)
  mobile = models.CharField(max_length=150, blank=False, null=False)
  agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, blank=True, null=True)
  class Meta:
        ordering = ['idNo']
  def __int__(self):
    return self.accountNo
  
class Payment(models.Model):
   amount = models.IntegerField(blank=False, null=False)
   account_type = models.CharField(max_length=50, blank=False, null=False)
   customer= models.OneToOneField(Customer, on_delete=models.SET_NULL, blank=True, null=True)
   pass 
   def __str__(self):
      return self.customer
  