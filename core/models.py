from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    reg_date = models.DateTimeField(default=timezone.now)

    def register_person(self):
        self.reg_date = timezone.now()
        self.save()
