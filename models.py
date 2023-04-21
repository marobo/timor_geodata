from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class Aldeia(models.Model):
    name = models.CharField(max_length=124)
    geom = models.PointField()

    def __str__(self):
        return self.name


class Suco(models.Model):
    name = models.CharField(max_length=124)
    district_name = models.CharField(max_length=124)
    subdistrict_name = models.CharField(max_length=124)
    geom = models.PolygonField()

    def __str__(self):
        return self.name

class Subdistrict(models.Model):
    name = models.CharField(max_length=124)
    geom = models.MultiPolygonField()

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=124)
    geom = models.MultiPolygonField()

    def __str__(self):
        return self.name
