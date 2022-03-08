# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 21:11:59 2022

@author: ladat
"""


from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
  path('',views.index),
  path('<slug:id>/', views.custom_date),
]