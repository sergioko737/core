from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
# Create your models here.

class Person(models.Model): #model of Person
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    reg_date = models.DateTimeField(default=timezone.now)

    def register_person(self):
        self.reg_date = timezone.now() #time of registration
        self.save()

    def __str__(self): #display registered details in admin site
        return str(self.last_name + ' ' + self.first_name + ' - ' + self.email)
