from django.contrib.gis import admin
from .models import Incident, County
from leaflet.admin import LeafletGeoAdmin


class IncidentAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')


class CountyAdmin(admin.GeoModelAdmin):
    list_display = ('name', 'geoid', 'statefp', 'countyns')
    search_fields = ['name', 'statefp']


admin.site.register(County, CountyAdmin)
admin.site.register(Incident, IncidentAdmin)


