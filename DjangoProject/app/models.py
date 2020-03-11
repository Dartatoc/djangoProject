"""
Definition of models.
"""
#def __unicode__(self):
#  return "{0} {1} {2} [{3}] [{4}]".format(self.name, self.description, self.type, self.currentStock, self.minimumStock)

from django.db import models

# Create your models here.
class Product(models.Model):
 name = models.CharField(max_length=100)
 description = models.CharField(max_length=100)
 type = models.CharField(max_length=100)
 currentStock = models.IntegerField()
 minimunStock = models.IntegerField()