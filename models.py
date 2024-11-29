from django.contrib.gis.db import models


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


# NEW TLS_ADM_FILES
class TLS_adm0(models.Model):
    name = models.CharField(max_length=124)
    geom = models.PolygonField()

    def __str__(self):
        return self.name


class TLS_adm1(models.Model):
    name = models.CharField(max_length=124)
    adm0_name = models.CharField(max_length=124)
    adm1_name = models.CharField(max_length=124)
    geom = models.MultiPolygonField()

    def __str__(self):
        return self.name


class TLS_adm2(models.Model):
    name = models.CharField(max_length=124)
    geom = models.MultiPolygonField()

    def __str__(self):
        return self.name


class TLS_adm3(models.Model):
    name = models.CharField(max_length=124)
    geom = models.MultiPolygonField()

    def __str__(self):
        return self.name
