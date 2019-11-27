#! python3.8
# -*- coding: utf-8 -*-

# File name:    gigfinder.py
# Author:       Tobias Rosskopf
# Email:        tobirosskopf@gmail.com
# Created:      27.11.2019
# Modified:     27.11.2019

"""
TODO:
Module's docstring
"""

# Standard imports
import sqlite3
import urllib.parse
# import urllib.request

# Third party imports
import requests
from bs4 import BeautifulSoup

# Package imports
from gigfinder.geocoder import address_to_lat_lng
from gigfinder.shpwriter import lat_lng_to_shp

# TODO: urllib --> requests!!!!


def main():
    """Main method"""

    conn = sqlite3.connect('gig_db.sqlite3')

    conn.execute('''
    CREATE TABLE "event" (
        "ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "PLZ"	INTEGER,
        "DATE"	TEXT,
        "PLACE"	TEXT,
        "ORGANISATOR"	TEXT,
        "LAT"	REAL,
        "LNG"	REAL
    );''')

    list_lat_lng = []

    for month in range(12):
        try:
            url_args = {
                "f3": str(month+1), # Monat
                "jahr": "2019",     # Jahr
                "seite": "1",       # Seite
                "index": "7",       # nach Termin aufsteigend
                }

            url = "http://www.kirmeskalender.de/liste.php?{}".format(urllib.parse.urlencode(url_args))
            # print(url)
            # request = urllib.request.urlopen(url)
            response = requests.get(url)
            response.raise_for_status()
            #html = request.read()
            soup = BeautifulSoup(response.text, "html.parser")
            
            # with open("out.html", "w") as f:
            #     f.write(str(soup))
        except Exception as ex:
            print("Server nicht erreichbar!")
            print(ex)

        try:
            for event in soup.find_all("div", {"class": "clear_both"}):
                if event.text:
                    plz = event.find("div", {"class": "liste_plz"}).text.strip()
                    ort = event.find("div", {"class": "liste_ort"}).text.strip()
                    termin = event.find("div", {"class": "liste_termin"}).text.strip()
                    org = event.find("div", {"class": "liste_kibu"}).text.strip()

                    print("{0} {1} - {2} - {3}".format(plz, ort, termin, org))

                    lat, lng = address_to_lat_lng(plz=plz, country="Germany")
                    list_lat_lng.append((float(lat), float(lng)))
                    # print("{0:.6f}, {1:.6f}".format(lat, lng))

                    conn.execute("INSERT INTO event (PLZ, PLACE, DATE, ORGANISATOR, LAT, LNG) VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '{5}')".format(plz, ort, termin, org, lat, lng))

        except Exception as ex:
            print(ex)

    conn.commit()
    conn.close()

    lat_lng_to_shp(list_lat_lng)


if __name__ == '__main__':
    main()
