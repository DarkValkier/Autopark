from datetime import datetime

from django.db import models


class Driver(models.Model):
    first_name = models.CharField('Имя', max_length=32)
    last_name = models.CharField('Фамилия', max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.created_at} {self.updated_at}'


class Vehicle(models.Model):
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE, null=True)
    make = models.CharField('Производитель', max_length=32)
    model = models.CharField('Модель', max_length=32)
    plate_number = models.CharField('Номерной знак', max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
