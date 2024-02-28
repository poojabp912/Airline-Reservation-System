from django.db import models

# Create your models here.
class EmpInsert(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    date = models.DateField(blank=True)
    phno = models.CharField(max_length=15)
    class Meta:
        db_table = 'user'