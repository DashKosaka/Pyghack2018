# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 23:03:56 2018

@author: Dash
"""
import requests
import numpy as np
import pandas as pd
import os

def get_data(building):
    
    url = 'https://maps.googleapis.com/maps/api/geocode/json?&key=AIzaSyBJUuDqdMW83obU_8PlGVwwNrVx9lxNAQM' + \
            '&address=' + building + '%20champaign'
            
    try:info = requests.get(url)
    except:print('Request Denied')
    
    ret = info.json()
    
    return ret

def get_location(jsn):
    
    try:
        return jsn['results'][0]['geometry']['location']
    except:
        print(jsn)
        os.exit('Uhoh....')
        
df = pd.read_csv('sp2017_plus.csv')

locations = []
mapping = {'ARR Inst Labor &  Industrial Rel': {'lat':40.105419, 'lng':-88.235832}}
for b in df.Building:
    
    if b not in mapping:
        mapping[b] = get_location(get_data(b))
    locations.append(mapping[b])

locations_ = np.array(locations)
df['Location'] = locations_

enrolled = []
grades = np.array(df[['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']].iloc[:,:])
for g in grades:
    enrolled.append(sum(g))

df['Total'] = np.array(enrolled)
    

df.to_csv('sp2017_final.csv', sep=',')



