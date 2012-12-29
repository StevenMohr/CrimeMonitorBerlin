from django.contrib.gis.db import models
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
    area = ForeignKey('OSMPolygon')
    
    def __unicode__(self):
        return self.name
    

class OSMPolygon:
    osm_id = models.AutoField(primary_key=True)
    way = models.PolygonField()
    
    class Meta:
        db_table = "planet_osm_polygon"
        managed = False
        
    objects = models.GeoManager()

