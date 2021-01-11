# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:09:50 2017
"""

import requests

def getelev(latitude, longitude):

    url = "http://ned.usgs.gov/epqs/pqs.php?x="+longitude+"&y="+latitude+"&units=Feet&output=json"
    resp = requests.get(url=url)
    json_out=resp.json()
    json_out = json_out['USGS_Elevation_Point_Query_Service']
    json_out = json_out['Elevation_Query']
    elevationquery = json_out['Elevation']  
    return(elevationquery)

x = getelev('40.38697','-104.59129')

print(x)
