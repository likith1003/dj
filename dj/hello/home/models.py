from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(("name"), max_length=50)
    pno=models.CharField(("pno"), max_length=50)
    email=models.CharField(("email"), max_length=50)
    gender=models.CharField(("gender"), max_length=50)
    dob=models.CharField(("dob"), max_length=50)
    password=models.CharField(("password"), max_length=50)
    def __str__(self):
        return self.name

class Expdata(models.Model):
    name=models.CharField(("name"), max_length=50)
    pno=models.CharField(("pno"), max_length=50)
    email=models.CharField(("email"), max_length=50)
    yop=models.CharField(("Year of Pass"), max_length=50)
    gender=models.CharField(("gender"), max_length=50)
    dob=models.CharField(("dob"), max_length=50)
    password=models.CharField(("password"), max_length=50)
    def __str__(self):
        return self.yop
class doners(models.Model):
    name=models.CharField((""), max_length=50)
    pno=models.CharField((""), max_length=50)
    email=models.CharField((""), max_length=50)
    bgroop=models.CharField((""), max_length=50)
    address=models.CharField((""), max_length=50)