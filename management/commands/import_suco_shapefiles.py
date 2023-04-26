from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping
from timor_geodata.models import Suco

class Command(BaseCommand):
    help = 'Import models from shapefiles'

    def handle(self, *args, **options):
        path_of_shp = './timor_geodata/shapefiles/Suco.shp'
        suco_mapping = {
            'name': 'SUCONAME',
            'district_name': 'DISTNAME',
            'subdistrict_name': 'SUBDISTRCT',
            'geom': 'POLYGON'
        }
        try:
            lm = LayerMapping(Suco, path_of_shp, suco_mapping, transform=False)
            lm.save(strict=True, verbose=True)
            self.stdout.write(self.style.SUCCESS('Successfully imported Sucos'))
        except:
            raise CommandError('Error importing Sucos')
