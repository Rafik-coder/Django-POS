from django.db import models
from django.utils import timezone


# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)
    date_employed = models.DateField(default=timezone.now)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    # class Meta:
    #     search_fields = ['name']


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Products(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    expiry_date = models.DateField()
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # class Meta:
    #     search_fields = ['name']


class Selected(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    qnt = models.IntegerField(default=0)


class Sales(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    qnt = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
