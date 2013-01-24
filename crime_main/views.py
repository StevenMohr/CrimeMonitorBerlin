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
        kwargs['districts'] = District.objects.all()
        return arguments
