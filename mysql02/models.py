from django.db import models
class manhuainfo(models.Model):

    num = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    com = models.CharField(max_length=1000)
    new = models.CharField(max_length=255)
    pop = models.IntegerField(null=True)
    type = models.CharField(max_length=255)
    pho=models.CharField(max_length=255)
    link=models.CharField(max_length=255)

class maninfo(models.Model):

    usernum = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    on = models.IntegerField(default=0)
    off = models.IntegerField(default=0)
    change = models.IntegerField(default=0)
    admin = models.IntegerField(default=0)



# Create your models here.
