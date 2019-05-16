from django.db import models
# Create your models here.

class Item(models.Model):
    number = models.CharField(max_length=7)
    description = models.TextField()
    p182_conversion = models.DecimalField(max_digits= 17, decimal_places= 16)
