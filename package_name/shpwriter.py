# -*- coding: iso-8859-1 -*-
# python 3.7

'''
Created on 27.11.2019
Modified on 27.11.2019

@author: Tobias Rosskopf
'''

# Imports
import shapefile


def lat_lng_to_shp(list_lat_lng):
    with shapefile.Writer('out') as w:
        w.field('NR', 'N')
        w.field('LAT', 'F', decimal=10)
        w.field('LNG', 'F', decimal=10)

        nr = 0
        for (lat, lng) in list_lat_lng:
            nr += 1
            # print("{0:.6f}, {1:.6f}".format(lat, lng))
            w.point(lng, lat)
            w.record(nr, lat, lng)
