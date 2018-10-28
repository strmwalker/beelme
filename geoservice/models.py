from django.db import models
from django.contrib.gis.db import models as gis_models


# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='geoservice/photos/places')
    location = gis_models.PointField()

    def __str__(self):
        return self.name
