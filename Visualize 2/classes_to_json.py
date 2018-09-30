# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 21:33:46 2018

@author: Dash
"""
# File before web crawling
import pandas as pd
import json

#{'AAS': 100: [crnsssss, dasfa sdf, asdf], 120, 300}

df = pd.read_csv('dataset.csv')

subjects = list(set(df.Subject))
jasons_big_file = {i: {} for i in subjects}
for s in subjects:
    curr_df = df[df.Subject == s].iloc[:,:3]
    
    numbers = list(set(curr_df.Course))
    for n in numbers:
        crns = list(curr_df[curr_df.Course == n].CRN)
        
        jasons_big_file[s][n] = crns
    
with open('classes_data.json', 'w') as outfile:
    json.dump(jasons_big_file, outfile)



