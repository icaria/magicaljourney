from django.db import models


# Create your models here.


class League(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=30)


class Division(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=30)


class Account(models.Model):
    id = models.BigIntegerField(primary_key=True)
    league = models.ForeignKey(League)
    division = models.ForeignKey(Division)
    name = models.CharField(max_length=50)
    level = models.BigIntegerField()
    is_online = models.BinaryField()
    last_updated = models.DateTimeField()


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account)
    message = models.CharField(max_length=1024)
    date_time = models.DateTimeField()
