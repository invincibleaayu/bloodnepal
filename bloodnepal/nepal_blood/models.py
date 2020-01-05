from django.db import models

class getInvolved(models.Model):
    name=models.CharField(max_length=40,blank=True, null=True)
    address=models.CharField(max_length=50,default="")
    dateOfBirth=models.DateField(blank=True, null=True)
    occupation=models.CharField(max_length=50,default="")
    phoneNo=models.IntegerField(default="")
    email=models.CharField(max_length=100,default="")
    gender=models.CharField(max_length=10)
    bloodGroup=models.CharField(max_length=5)
    RH_type=models.CharField(max_length=5)
    ques_1=models.CharField(max_length=105,default="")
    ques_2=models.CharField(max_length=105,default="")


class Donate(models.Model):
    name=models.CharField(max_length=40,blank=True, null=True)
    address=models.CharField(max_length=50,default="")
    phoneNo=models.IntegerField(default="")
    email=models.CharField(max_length=100,default="")
    gender=models.CharField(max_length=10)
    bloodGroup=models.CharField(max_length=5)
    RH_type=models.CharField(max_length=5)
