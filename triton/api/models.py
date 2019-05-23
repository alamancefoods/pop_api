from django.db import models
# Create your models here.

class Item(models.Model):
    number = models.CharField(max_length=7)
    description = models.TextField()
 ProdGoal(models.Model):
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

