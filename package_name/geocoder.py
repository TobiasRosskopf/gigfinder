# -*- coding: iso-8859-1 -*-
# python 3.7

'''
Created on 27.11.2019
Modified on 27.11.2019

@author: Tobias Rosskopf
'''

# Imports
from opencage.geocoder import OpenCageGeocode

key = 'd1be2f38749d4c90914fcbfe1ebf25a1'
geocoder = OpenCageGeocode(key)

def address_to_lat_lng(street="", nr="", plz="", city="", country=""):
    address = "{0} {1}, {2} {3}, {4}".format(street, nr, plz, city, country)

    result = geocoder.geocode(address)

    r = result[0]
    lat = r['geometry']['lat']
    lng = r['geometry']['lng']

    return lat, lng
