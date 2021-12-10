from django.db import models
from django.utils.html import format_html

# Create your models here.
class Persona(models.Model):

    first_name     = models.CharField(max_length=50)
    last_name      = models.CharField(max_length=50)
    address_street = models.CharField(max_length=100)
    address_number = models.IntegerField()
    city           = models.CharField(max_length=50)
    postcode       = models.IntegerField()
    country        = models.CharField(max_length=50)
    email          = models.CharField(max_length=50)
    username       = models.CharField(max_length=50)
    password       = models.CharField(max_length=50)
    age            = models.IntegerField()
    picture        = models.CharField(max_length=200)

    def __str__(self):
        return f"Persona {self.first_name} {self.last_name} ({self.id})"
