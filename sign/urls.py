from django.contrib import admin
from django.urls import path
from . import views
# from flight.views import addfl

urlpatterns = [
    path('', views.Insertrecord,name='Insertrecord'),
]