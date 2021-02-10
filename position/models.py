from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    wage = models.DecimalField(decimal_places=2, max_digits=10)
    bonus = models.DecimalField(decimal_places=2, max_digits=10)
    bond_type = models.CharField(max_length=50)
