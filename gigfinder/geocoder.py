#! python3.8
# -*- coding: utf-8 -*-

# File name:    geocoder.py
# Author:       Tobias Rosskopf
# Email:        tobirosskopf@gmail.com
# Created:      27.11.2019
# Modified:     27.11.2019

"""
TODO:
Module's docstring
"""

# Standard imports
# ---

# Third party imports
from opencage.geocoder import OpenCageGeocode

# Package imports
from gigfinder.secrets import OPENCAGE_APIKEY


# Get API key and create geocoder
geocoder = OpenCageGeocode(OPENCAGE_APIKEY)


def address_to_lat_lng(street="", nr="", plz="", city="", country=""):
    """TODO: Docstring"""

    address = "{0} {1}, {2} {3}, {4}".format(street, nr, plz, city, country)

    result = geocoder.geocode(address)

    r = result[0]
    lat = r['geometry']['lat']
    lng = r['geometry']['lng']

    return lat, lng
