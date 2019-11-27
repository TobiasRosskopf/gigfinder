# -*- coding: iso-8859-1 -*-
# python 3.7

'''
Created on 09.09.2019
Modified on 27.11.2019

@author: Tobias Rosskopf
'''

# Imports
import sqlite3
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

import geocoder
import shpwriter

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
        request = urllib.request.urlopen(url)
        html = request.read()
        soup = BeautifulSoup(html, "html.parser")
        
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

                lat, lng = geocoder.address_to_lat_lng(plz=plz, country="Germany")
                list_lat_lng.append((float(lat), float(lng)))
                # print("{0:.6f}, {1:.6f}".format(lat, lng))

                conn.execute("INSERT INTO event (PLZ, PLACE, DATE, ORGANISATOR, LAT, LNG) VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '{5}')".format(plz, ort, termin, org, lat, lng))

            

    except Exception as ex:
        print(ex)

conn.commit()
conn.close()

shpwriter.lat_lng_to_shp(list_lat_lng)

# try:
#     table = soup.find("table")
#     rows = table.find_all("tr")

#     data = []
#     for row in rows:
#         cols = row.find_all('td')
#         cols = [ele.text.strip() for ele in cols]
#         data.append([ele for ele in cols if ele]) 

#     for row in data[1:]:
#         if len(row) > 0:
#             output = " %s: 1. %s \n     2. %s\n" % (row[1].upper(), row[0].replace("\n", " "), row[2].replace("\n", " "))
#             print(output)

# except Exception as ex:
#     print(ex)
