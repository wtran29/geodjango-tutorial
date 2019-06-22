from django.contrib.gis import admin
from .models import Incident
from leaflet.admin import LeafletGeoAdmin


class IncidentAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')


admin.site.register(Incident, IncidentAdmin)
