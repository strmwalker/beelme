from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.
from django.db.models import signals
from tastypie.models import create_api_key


class Place(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='geoservice/photos/places')
    location = gis_models.PointField()

    def __str__(self):
        return self.name


signals.post_save.connect(create_api_key, sender=User)
