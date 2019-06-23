from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, DetailView
from django.core.serializers import serialize

from .models import County, Incident


class HomePageView(TemplateView):
    template_name = 'incidents/index.html'


def county_datasets(request):
    counties = serialize('geojson', County.objects.filter(geoid='06037'))
    return HttpResponse(counties, content_type='json')


def incident_data(request):
    points = serialize('geojson', Incident.objects.all())
    return HttpResponse(points, content_type='json')
