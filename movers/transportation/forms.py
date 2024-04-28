from .models import order
from django.contrib.auth.models import User
from django import forms

class make_order(forms.ModelForm):
    
    class Meta:
        model=order
        fields=['source','destination','approx_weight','descriptive_text']