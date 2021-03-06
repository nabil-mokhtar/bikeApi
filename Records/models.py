from django.db import models
from Users.models import User
from Products.models import Bike, accessories

# Create your models here.


class RentRecords(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    starts = models.DateTimeField()
    ends = models.DateTimeField()
    status = models.CharField(max_length=10)
    note = models.CharField(max_length=50)
    price = models.IntegerField()
   # adminName=models.TextField(max_length=100)
    def __str__(self):
        return self.status


class FixRecords(models.Model):
    # we need to make defult customer to unsaved users
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    price = models.IntegerField()
    dateTime = models.DateTimeField(auto_now=True)
    notes = models.TextField(max_length=100)


class SellBRecord(models.Model):
    # we need to make defult customer to unsaved users
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    price = models.IntegerField()
    bike = models.ForeignKey(Bike, on_delete=models.PROTECT)
    dateTime = models.DateTimeField()
    notes = models.TextField()
  #  adminName=models.TextField(max_length=100)

class SellARecord(models.Model):
    # we need to make defult customer to unsaved users
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    price = models.IntegerField()
    accessorie = models.ForeignKey(accessories, on_delete=models.PROTECT)
    dateTime = models.DateTimeField()
    notes = models.TextField()
  #  adminName=models.TextField(max_length=100)

class Noterecord(models.Model):
    # we need to make defult customer to unsaved users
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    price = models.IntegerField()
    note = models.TextField(max_length=100)
