# Create your views here.
from django.db.models.aggregates import Count
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from crime_main.models import Crime, District

class MainView(ListView):
    template_name = "main.html"
    queryset = Crime.objects.all()
    context_object_name = "crimes"

    def get_context_data(self, **kwargs):
        arguments = kwargs
        districts = District.objects.all()
        kwargs['districts'] = districts
        geo_districts = [x.way for x in districts ]
        berlin_borders = geo_districts[0]
        for geo in geo_districts[1:]:
            berlin_borders = berlin_borders.union(geo)
        kwargs['center'] = berlin_borders.centroid
        kwargs['crimes'] = Crime.objects.all().order_by('pub_date')
        return arguments
