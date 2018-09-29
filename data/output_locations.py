# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:16:44 2018

@author: Dash
"""
import numpy as np
import pandas as pd
import csv

df = pd.read_csv('Courses.csv')

loc = df.Location

new_loc = pd.Series.dropna(loc)
new_loc = new_loc[new_loc != '-']
new_loc = new_loc[new_loc != 'Location']

rooms = set(new_loc)

mapping = list(map(lambda x: x.split('-'), rooms))
buildings = [x[-1] for x in mapping]
buildings = np.array(set(buildings))

with open('buildings.csv', 'wb') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(buildings)






