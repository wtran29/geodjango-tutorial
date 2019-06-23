from django.urls import path
from .views import HomePageView, county_datasets, incident_data

app_name = 'incidents'
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('county_data/', county_datasets, name='county'),
    path('incident_data/', incident_data, name='incident'),
]
