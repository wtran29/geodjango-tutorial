from django.contrib.gis.db import models


class Incident(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)

    # objects = models.GeoManager()

    def __str__(self):
        return self.name

