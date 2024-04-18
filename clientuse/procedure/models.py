from django.db import models
from django.urls import reverse
# Create your models here.
class Clients(models.Model):
    score=models.CharField(max_length=16)
    surname=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    Otchestvo=models.CharField(max_length=20)
    DateofBirth=models.DateField()
    INN=models.IntegerField()
    FIO=models.ForeignKey('User',on_delete=models.PROTECT,null=True)
    status=models.ForeignKey('Status',on_delete=models.PROTECT,default=1)
    def get_absolute_url(self):
        return reverse('up',kwargs={'clientid':self.pk})
class Status(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class User(models.Model):
    FIO=models.CharField(max_length=100)
    Login=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    def __str__(self):
        return self.FIO


