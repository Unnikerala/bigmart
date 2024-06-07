from django.db import models


class productdb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    subject = models.CharField(max_length=100,null=True,blank=True)
    message = models.CharField(max_length=100,null=True,blank=True)


class registerdb(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)


class cartdb(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Productname = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(max_length=100,null=True,blank=True)
    Totalprice = models.IntegerField(max_length=100,null=True,blank=True)