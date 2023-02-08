from django.db import models

# Create your models here.
class Musteri(models.Model):
    date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=16, blank=True, null=True)
    tel = models.CharField(max_length=64, blank=True, null=True)
    brand = models.CharField(max_length=32, blank=True, null=True)
    model = models.CharField(max_length=64, blank=True, null=True)
    reason = models.CharField(max_length=64, blank=True, null=True)
    solution = models.CharField(max_length=64, blank=True, null=True)
    price = models.CharField(max_length=8, blank=True, null=True)
    fin_date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)
    cabel = models.BooleanField(default=False)
    remote = models.BooleanField(default=False)
    foot = models.BooleanField(default=False)
    drzac = models.BooleanField(default=False)
    module = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    content = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.title

class Company(models.Model):
    logo = models.ImageField(upload_to="static/customer/logo", blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    location = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=32, blank=True, null=True)

class Doc(models.Model):
    content = models.CharField(max_length=4096, blank=True, null=True)