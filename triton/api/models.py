from django.db import models
# Create your models here.

class Item(models.Model):
    number = models.CharField(max_length=7)
    description = models.TextField()
    p182_conversion = models.DecimalField(max_digits= 17, decimal_places= 16)


class Employee(models.Model):
    emp_id = models.CharField(max_length = 20)
    first_name = models.CharField(max_length = 20)
    middle_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    suffix = models.CharField(max_length = 3, blank=True)
    birth_date = models.DateField()
    language = models.CharField(max_length = 3)
    supervisor = models.BooleanField()
    manager = models.BooleanField()
    certificates = models.TextField(max_length = 240)
    med_restrictions = models.TextField(max_length = 480)


class Shift(models.Model):
    number = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Line(models.Model):
    number = models.CharField(max_length = 2)


class Machine(models.Model):
    name = models.CharField(max_length = 1)
    line = models.ForeignKey(Line, null=True, on_delete= models.SET_NULL)


# Definitely skeptical of setting item to null. Likely to be revised...
class ProdGoal(models.Model):
    date = models.DateField(db_index=True)
    quantity = models.IntegerField()
    item = models.ForeignKey(Item, null=True, on_delete= models.SET_NULL)

    class Meta:
        unique_together = [['date', 'item']]


"""
Here's the proverbial Big Kahuna. The Product Snapshot table
(ProdSnap for ease of typeing) will contain information on a single production
instance. Ideally, it will get pretty granular, but it will likely be updated
on an hourly basis initially.
"""
class ProdSnap(models.Model):
    shifts = models.ManyToManyField(Shift)
    employees = models.ManyToManyField(Employee)
    line = models.ForeignKey(Line, null=True, on_delete= models.SET_NULL)
    machines = models.ManyToManyField(Machine)
    item = models.ForeignKey(Item, null=True, on_delete= models.SET_NULL)
    quant = models.IntegerField()
    date = models.DateField()
    timestamp = models.DateTimeField(db_index= True, auto_now_add= True)

