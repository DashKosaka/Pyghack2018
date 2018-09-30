# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 19:31:10 2018

@author: Dashiell
"""
import requests, re, winsound, sys, time, random
import numpy as np
from string import digits

# year, sem, major, course = input('[Year] [fall/spring/summer] [Major] [Course Number]\n').split()

file = 'courses.txt'
courses = list(map(lambda x: x.replace('\n', '').split(','), open(file).readlines()))

def find_course(year, sem, major, course):
    
    # print('\nFinding course\n')
    
    try:
        response = requests.get('https://courses.illinois.edu/search/schedule/%s/%s/%s/%s' % (year, sem, major, course))

        # print('Webpage found')

    except:
        
        sys.exit('Webpage could not be found')

    return response

def check_available(CRN, response):

    CRN_pattern = "crn.*?" + CRN

    r_info = re.findall(r'({"status".*?})', response.text)
    
    for section in r_info:
        
        CRN_found = re.search(r'%s' % (CRN_pattern), section)
        
        
        if(CRN_found):
            
            time_pattern = 'time.*?app-meeting.*?>(.*?)<'
            time = re.findall(r'%s' % (time_pattern), section)[0]
            
            location_pattern = 'location.*?>(.*?)<'
            location = re.findall(r'%s' % (location_pattern), section)[0]            
            remove_digits = str.maketrans('', '', digits)
            location = location.translate(remove_digits).strip()
            
            day_pattern = 'day.*?>([\w]{1,2}).*?<'
            day = re.findall(r'%s' % (day_pattern), section)[0]
            
            return (time, day, location)
    
    print('Could not find section with CRN = %s' % (CRN))
    
    return 'Error'
        
# Alerter Loop
print('Starting search')
beep_alert()
counter = 0
frequency = 60
while(1):
    
    print('Times searched:', counter)

    for course in courses:
        
        alerter(*course)    
    
    for i in range(frequency):
 
        time.sleep(1) 
        
    time.sleep(random.randint(0, 10))
    
    counter += 1

