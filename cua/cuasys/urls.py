from django.urls import path
from . import views
urlpatterns=[
  path('login/',views.login, name='login'),
  path('',views.dashboard, name='dashboard'),
  path('customer/<int:idNo>',views.customer, name='customer'),
  path('notification/',views.notification, name='notification'),

]