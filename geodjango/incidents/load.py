import os
from django.contrib.gis.utils import LayerMapping
from .models import County

county_mapping = {
    'statefp': 'STATEFP',
    'countyfp': 'COUNTYFP',
    'countyns': 'COUNTYNS',
    'geoid': 'GEOID',
    'name': 'NAME',
    'namelsad': 'NAMELSAD',
    'lsad': 'LSAD',
    'classfp': 'CLASSFP',
    'mtfcc': 'MTFCC',
    'csafp': 'CSAFP',
    'cbsafp': 'CBSAFP',
    'metdivfp': 'METDIVFP',
    'funcstat': 'FUNCSTAT',
    'aland': 'ALAND',
    'awater': 'AWATER',
    'intptlat': 'INTPTLAT',
    'intptlon': 'INTPTLON',
    'geom': 'MULTIPOLYGON',
}

county_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'tl_2017_us_county.shp')
)


def run(verbose=True):
    lm = LayerMapping(County, county_shp, county_mapping, transform=False, encoding='ISO-8859-1')
    lm.save(strict=True, verbose=verbose)
