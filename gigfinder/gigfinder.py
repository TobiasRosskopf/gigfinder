#! python3.8
# -*- coding: utf-8 -*-

# File name:    gigfinder.py
# Author:       Tobias Rosskopf
# Email:        tobirosskopf@gmail.com
# Created:      27.11.2019
# Modified:     29.11.2019

"""
TODO:
Module's docstring
"""

# Standard imports
import sqlite3
import urllib.parse

# Third party imports
import requests
from bs4 import BeautifulSoup

# Package imports
import geocoder
import shpwriter


def main():
    """Main method"""

    conn = sqlite3.connect('gig_db.sqlite3')

    conn.execute('''
    CREATE TABLE "event" (
        "ID"            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "PLZ"           INTEGER,
        "DATE"          TEXT,
        "PLACE"         TEXT,
        "ORGANISATOR"   TEXT,
        "LAT"           REAL,
        "LNG"           REAL
    );''')

    list_lat_lng = []

    for year in range(2019, 2023):
        for month in range(12):
            try:
                url_args = {
                    "f3": str(month+1), # Monat
                    "jahr": year,       # Jahr
                    "seite": "1",       # Seite
                    "index": "7",       # nach Termin aufsteigend
                    }

                url = "http://www.kirmeskalender.de/liste.php?{}".format(urllib.parse.urlencode(url_args))
                response = requests.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")

            except Exception as ex:
                print("Server nicht erreichbar!")
                print(ex)

            try:
                for event in soup.find_all("div", {"class": "clear_both"}):
                    if event.text:
                        plz = event.find("div", {"class": "liste_plz"}).text.strip()
                        city = event.find("div", {"class": "liste_ort"}).text.strip()
                        date = event.find("div", {"class": "liste_termin"}).text.strip()
                        org = event.find("div", {"class": "liste_kibu"}).text.strip()

                        print("{2} {3} ({0} {1})".format(plz, city, date, org))

                        lat, lng = geocoder.address_to_lat_lng(plz=plz, city=city, country="Germany")
                        list_lat_lng.append((float(lat), float(lng)))
                        # print("{0:.6f}, {1:.6f}".format(lat, lng))

                        conn.execute("INSERT INTO event (PLZ, PLACE, DATE, ORGANISATOR, LAT, LNG) VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '{5}')".format(plz, city, date, org, lat, lng))

            except Exception as ex:
                print(ex)

        conn.commit()

    conn.close()

    shpwriter.lat_lng_to_shp(list_lat_lng)


if __name__ == '__main__':
    main()
