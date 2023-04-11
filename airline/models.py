from django.db import models
from django.contrib.auth.models import User
import uuid

class EmpInsert(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    date = models.DateField(blank=True)
    phno = models.CharField(max_length=10)
    class Meta:
        db_table = 'user'

class Feedbac(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    feedba = models.CharField(max_length=50)
    rating = models.IntegerField()
    eid = models.ForeignKey(EmpInsert,on_delete=models.CASCADE,related_name='disp')
    class Meta:
        db_table = 'Feedback'

class fli(models.Model):
    fname = models.CharField(max_length=20)
    sour = models.CharField(max_length=20)
    dest = models.CharField(max_length=20)
    price = models.CharField(max_length=8)
    seat = models.IntegerField()
    class Meta:
        db_table = 'Flights'

class book(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    sour = models.CharField(max_length=20)
    dest = models.CharField(max_length=20)
    date = models.DateField(blank=True)
    seats = models.IntegerField()
    eid = models.ForeignKey(EmpInsert,on_delete=models.CASCADE,related_name='dis')
    fid = models.ForeignKey(fli,on_delete=models.CASCADE,related_name='disp')
    price = models.CharField(max_length=8)
    pay = models.CharField(max_length=6)
    rand = models.IntegerField()
    # new = models.IntegerField()