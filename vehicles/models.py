from django.db import models
from users.models import Owner, Agent

import uuid 

# Create your models here.
"""
Model for vehicles
"""
class Vehicles(models.Model):
    transaction_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    car_reg_no = models.CharField(primary_key=True, max_length=100)
    car_make = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    hash = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Vehicle: {}".format(self.car_reg_no)

    class Meta:
        db_table = 'vehicles'

"""
Model for vehicles transactions ==== Registration, Transfer, Confirmation
"""
class Transactions(models.Model):
    # block_id = models.AutoField(auto_created=True)
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    car_reg = models.ForeignKey(Vehicles, on_delete=models.CASCADE, null=True, related_name='related_transactions')
    national = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, related_name='related_transactions')
    kra = models.ForeignKey(Agent, on_delete=models.CASCADE, blank=True, related_name='related_transactions')
    status = models.CharField(max_length=100) # owned, transferred, pending
    previous_hash = models.CharField(max_length=100)
    hash = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Vehicle: {}".format(self.car_reg)

    class Meta:
        db_table = 'vehicle_transactions'