# Create your views here.
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from crime_main.models import Crime

class MainView(ListView):
    template_name = "main.html"
    queryset = Crime.objects.all()
    context_object_name = "crimes"
