from django.db import models

class getInvolved(models.Model):
    name=models.CharField(max_length=40,blank=True, null=True)
    address=models.CharField(max_length=50,default="")
    dateOfBirth=models.DateField(blank=True, null=True)
    occupation=models.CharField(max_length=50,default="")
    phoneNo=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=100,default="")
    gender=models.CharField(max_length=10)
    bloodGroup=models.CharField(max_length=5)
    RH_type=models.CharField(max_length=5)
    ques_1=models.CharField(max_length=105,default="")
    ques_2=models.CharField(max_length=105,default="")


class Donate(models.Model):
    name=models.CharField(max_length=40,blank=True, null=True)
    address=models.CharField(max_length=50,default="")
    phoneNo=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=100,default="")
    gender=models.CharField(max_length=10)
    bloodGroup=models.CharField(max_length=5)
    RH_type=models.CharField(max_length=5)

class app(models.Model):
    name = models.CharField(max_length = 220)
    op = models.IntegerField(default=0)
    on = models.IntegerField(default=0)
    ap = models.IntegerField(default=0)
    an = models.IntegerField(default=0)
    bp = models.IntegerField(default=0)
    bn = models.IntegerField(default=0)
    abp = models.IntegerField(default=0)
    abn = models.IntegerField(default=0)

class requestblood(models.Model):
    Full_Name=models.CharField(max_length=500)
    Address=models.CharField(max_length=500)
    Phone_Number=models.CharField(max_length=500)
    Email=models.CharField(max_length=500)
    blood_group=models.CharField(max_length=50)
    RH_type=models.CharField(max_length=50)

    def __str__(self):
        return "{}--{}--{}--{}--{}--{}--{}--{}".format(self.name,self.op,self.on,self.ap,self.an,self.bp,self.bn,self.abp,self.abn)
