from django.db import models

# Create your models here.

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  age = models.IntegerField(null=True)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

class Court(models.Model):
  name = models.CharField(max_length=255)
  form = models.CharField(max_length=255)
  locateCity = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.name}"
