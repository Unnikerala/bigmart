from django.db import models



class elementdb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    Category = models.CharField(max_length=100,null=True,blank=True)
    price = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='Product Images',null=True,blank=True)


class listdb(models.Model):
    categoryname = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    categorypic = models.ImageField(upload_to='list Images',null=True,blank=True)

# Create your models here.
