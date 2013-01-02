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
    area_id = models.IntegerField()
    way = models.GeometryField(blank=True, null=True)

    def __unicode__(self):
        return self.name

