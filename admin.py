from django.contrib.gis import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Aldeia, Suco, Subdistrict, District


class AldeiaAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    list_filter = ['name']

class SucoAdmin(admin.OSMGeoAdmin):
    list_display = ['name', 'subdistrict_name', 'district_name']
    list_filter = ['district_name', 'subdistrict_name']


class DistrictAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    list_filter = ['name']


class SubdistrictAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    list_filter = ['name']


admin.site.register(Suco, SucoAdmin)
admin.site.register(Aldeia, AldeiaAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Subdistrict, SubdistrictAdmin)
