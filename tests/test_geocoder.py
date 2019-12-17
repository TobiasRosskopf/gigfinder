#! python3.8
# -*- coding: utf-8 -*-

# File name:    test_geocoder.py
# Author:       Tobias Rosskopf
# Email:        tobirosskopf@gmail.com
# Created:      27.11.2019
# Modified:     27.11.2019

"""
Unittests for module geocoder.py.
"""

# Standard imports
import unittest

# Package imports
from gigfinder import geocoder


class TestGeocoder(unittest.TestCase):
    """TODO: Testclass' docstring"""

    def test_address_to_lat_lng_all(self):
        """TODO: Test's docstring"""
        street = "Pfungstädter Straße"
        nr = 20
        plz = 64297
        city = "Darmstadt"
        coords = (49.8169801, 8.641946)
        self.assertEqual(geocoder.address_to_lat_lng(street=street, nr=nr, plz=plz, city=city), coords)

    def test_address_to_lat_lng_city(self):
        """TODO: Test's docstring"""
        city = "Darmstadt"
        coords = (49.872775, 8.651177)
        self.assertEqual(geocoder.address_to_lat_lng(city=city), coords)


if __name__ == '__main__':
    unittest.main()
