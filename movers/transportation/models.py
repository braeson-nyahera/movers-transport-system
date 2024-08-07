from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class order(models.Model):
    order_title=models.CharField(max_length=100)
    source= models.CharField(max_length=100)
    destination= models.CharField(max_length=100)
    approx_weight= models.DecimalField(decimal_places=2, max_digits=10)
    descriptive_text=models.TextField(max_length=1000,null=True, blank=True)
    date_ordered=models.DateTimeField(default=timezone.now)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    transport_status={
        ('pending approval', 'pending approval' ),
        ('in-transit','in-transit' ),
        ('completed', 'completed'),
    }
    status=models.CharField(max_length=50, choices=transport_status,default='pending approval')
    
    def __str__(self):  
        return self.order_title