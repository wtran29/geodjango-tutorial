from django.shortcuts import render
from django.views.generic import TemplateView, DetailView


class HomePageView(TemplateView):
    template_name = 'incidents/index.html'


