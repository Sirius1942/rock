from django.db import models

# Create your models here.
class checkinlist(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    singner = models.CharField(max_length=100, blank=True, default='')
    
    class Meta:
        ordering = ['created_time']