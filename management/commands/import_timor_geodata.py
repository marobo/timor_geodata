from django.core.management.base import BaseCommand
from django.contrib.gis.utils import LayerMapping

from timor_geodata.models import TLS_adm0, TLS_adm1, TLS_adm2, TLS_adm3


class Command(BaseCommand):
    def handle(self, *args, **options):

        tls_adm0_shp = './tls_adm/tls_adm0.shp'
        tls_adm0_mapping = {
            'name': 'ADM0_EN',
            'geom': 'POLYGON'
        }

        tls_adm1_shp = './tls_adm/tls_adm1.shp'
        tls_adm1_mapping = {
            'name': 'ADM1_EN',
            'geom': 'POLYGON'
        }

        tls_adm2_shp = './tls_adm/tls_adm2.shp'
        tls_adm2_mapping = {
            'name': 'ADM2_EN',
            'adm0_name': 'ADM0_EN',
            'adm1_name': 'ADM1_EN',
            'geom': 'POLYGON'
        }

        tls_adm3_shp = './tls_adm/tls_adm3.shp'
        tls_adm3_mapping = {
            'name': 'ADM3_EN',
            'geom': 'POINT'
        }

        lm0 = LayerMapping(
            TLS_adm0, tls_adm0_shp, tls_adm0_mapping,
            transform=False, encoding='iso-8859-1',
            source_srs=4326
        )
        lm0.save(strict=True)

        lm1 = LayerMapping(
            TLS_adm1, tls_adm1_shp, tls_adm1_mapping,
            transform=False, encoding='iso-8859-1',
            source_srs=4326
        )
        lm1.save(strict=True)

        lm2 = LayerMapping(
            TLS_adm2, tls_adm2_shp, tls_adm2_mapping,
            transform=False, encoding='iso-8859-1',
            source_srs=4326
        )
        lm2.save(strict=True)

        lm3 = LayerMapping(
            TLS_adm3, tls_adm3_shp, tls_adm3_mapping,
            transform=False, encoding='iso-8859-1',
            source_srs=4326
        )
        lm3.save(strict=True)
