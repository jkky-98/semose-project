from django.db import models
from django.utils import timezone
# Create your models here.

class Place(models.Model):
    place_name = models.CharField(max_length=255)
    x = models.FloatField()
    y = models.FloatField()
    class Meta:
        app_label = 'api'
        db_table = 'places'
