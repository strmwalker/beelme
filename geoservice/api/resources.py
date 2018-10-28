from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geoip2 import GeoIP2
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.contrib.gis.resources import ModelResource
from tastypie import fields

from geoservice.models import Place

geo_ip2 = GeoIP2()


class PlaceResource(ModelResource):
    class Meta:
        filtering = {
            'distance': ('lte', 'lt')
        }
        queryset = Place.objects.all()
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()

    distance = fields.FloatField()

    def get_object_list(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip:
            point = geo_ip2.geos(ip)
        else:
            # let's show them our favorite tacos
            point = geo_ip2.geos('1.1.1.1')

        return super().get_object_list(request).annotate(distance=Distance('location', point))
