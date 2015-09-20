from django.db import models

# Create your models here.


class League(models.Model):
    LeagueId = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=30)

class Division(models.Model):
    DivisionId = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=30)

class Account(models.Model):
    AccountId = models.BigIntegerField()
    LeagueId = models.ForeignKey(League)
    DivisionId = models.ForeignKey(Division)
    Name = models.CharField(max_length=50)
    IsOnline = models.BinaryField()
    InGame = models.BinaryField()

class Notification(models.Model):
    NotificationId = models.AutoField(primary_key=True)
    AccountId = models.ForeignKey(Account)
    Message = models.CharField(max_length=1024)
    DateTime = models.DateTimeField()