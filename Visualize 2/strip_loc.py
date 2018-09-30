# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:12:00 2018

@author: Dash
"""

import numpy as np
import re
import json
import csv
import pandas as pd

df = pd.read_csv('sp2017_final.csv')

# Need - [Subject, Course, Start time, End time, Day, Building, Location, Total]
compress = df[['Subject', 'Course', 'CRN', 'Start time', 'End time', 'Day', 'Building', 'Location', 'Total']]

headers = list(compress.CRN)

jsn = {}
for index, r in df.iterrows():
    jsn[str(r.CRN)] = {'Subject':r.Subject, 'Course':r.Course, 'CRN':r.CRN, 'Start time':r['Start time'], 'End time':r['End time'], 'Day':r.Day, 'Building':r.Building, 'Location':r.Location, 'Total':r.Total}
    
with open('map_data.json', 'w') as outfile:
    json.dump(jsn, outfile)
