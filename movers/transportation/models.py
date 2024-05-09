from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class order(models.Model):
    source= models.CharField(max_length=100)
    destination= models.CharField(max_length=100)
    approx_weight= models.DecimalField(decimal_places=2, max_digits=10)
    descriptive_text=models.TextField()
    date_ordered=models.DateTimeField(default=timezone.now)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.id)
    
    