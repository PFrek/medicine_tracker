from django.db import models
from django.urls import reverse

# Create your models here.
class Medicine(models.Model):
    """Model representing a medicine."""
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class TimeSpot(models.Model):
    """Model representing a time spot for taking medicine."""
    name = models.CharField(max_length=200)
    time = models.TimeField()
    
    medicine = models.ManyToManyField(Medicine, help_text='Select the medicine that has to be taken in this time spot')
    
    def __str__(self):
        return f'{self.name} ({self.time})'
    
    def get_absolute_url(self):
        return reverse('timespot-list', args=[str(self.id)])
    
    def display_medicine(self):
        return ', '.join(medicine.name for medicine in self.medicine.all())
    
    display_medicine.short_description = 'Medicine'