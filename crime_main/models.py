from django.contrib.gis.db import models
from django.contrib.gis.geos import Polygon
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Crime(models.Model):
    districts = models.ManyToManyField('District')
    title = models.CharField(max_length = 200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    full_text_link = models.URLField(max_length = 800, unique=True)
    
    #Using geo-enabled object manager
    objects = models.GeoManager()
    
class District(models.Model):
    name = models.CharField(max_length = 200, unique=True)
    area_id = models.IntegerField()
    way = models.GeometryField(blank=True, null=True)

    def _polygon_wkt(self):
        poly = self.way.wkt
        return poly.replace('LINESTRING', 'POLYGON')

    polygon_wkt = property(_polygon_wkt)

    def _crime_ratio(self):
        crimes = self.crime_set.count()
        crime_total = Crime.objects.count()
        return crimes / float(crime_total)

    crime_ratio = property(_crime_ratio)

    def __unicode__(self):
        return self.name

