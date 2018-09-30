# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:12:00 2018

@author: Dash
"""

import numpy as np
import re
import json


with open('buildings2.csv', 'r') as f:
        
    data = (f.readlines())
    
new_data = list(map(lambda x: x.split(','), data))

jasons_file = {}
for i in data:
    try:
        lat, long = re.findall('-?\d+\.\d+', i)
        
        names = re.findall(',"(.*?)",', i)
        jasons_file[names[1]] = {'center':{'lat': float(lat), 'lng': float(long)}, 'population':10}
    except:
        pass
    
with open('data.json', 'w') as outfile:
    json.dump(jasons_file, outfile)
'''
for i in data:
    dec = re.findall('\d+\.\d+', i)
    names = re.findall(',".*?",', i)
    print(len(names))


lat = 
long = 

'''