#! python3.8
# -*- coding: utf-8 -*-

# File name:    shpwriter.py
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
import shapefile


def lat_lng_to_shp(list_lat_lng):
    """TODO: Docstring"""
    
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
