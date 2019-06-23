from django.contrib.gis.db import models


class Incident(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    location = models.PointField(srid=4326)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class County(models.Model):
    statefp = models.CharField(max_length=2)
    countyfp = models.CharField(max_length=3)
    countyns = models.CharField(max_length=8)
    geoid = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    namelsad = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    classfp = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    csafp = models.CharField(max_length=3)
    cbsafp = models.CharField(max_length=5)
    metdivfp = models.CharField(max_length=5)
    funcstat = models.CharField(max_length=1)
    aland = models.BigIntegerField()
    awater = models.BigIntegerField()
    intptlat = models.CharField(max_length=11)
    intptlon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'counties'
