# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 19:31:10 2018

@author: Dashiell
"""
import requests, re, winsound, sys, time, random
import numpy as np
from string import digits
import pandas as pd

pd.set_option('display.max_columns', 500)


# year, sem, major, course = input('[Year] [fall/spring/summer] [Major] [Course Number]\n').split()

def find_course(year, sem, major, course):
    # print('\nFinding course\n')

    try:
        response = requests.get('https://courses.illinois.edu/search/schedule/%s/%s/%s/%s' % (year, sem, major, course))

        # print('Webpage found')

    except:

        sys.exit('Webpage could not be found')

    return response


def convert_time_string_to_minutes(time_string):
    result = 0
    if time_string[-2:] == "PM":
        result += 60 * 12

    time_string = time_string[:-2].split(":")
    result += int(time_string[0]) * 60
    result += int(time_string[1])
    return result


def get_time_day_location(CRN, response):
    CRN_pattern = "crn.*?" + CRN

    r_info = re.findall(r'({"status".*?})', response.text)

    for section in r_info:

        CRN_found = re.search(r'%s' % (CRN_pattern), section)

        if (CRN_found):
            time_pattern = 'time.*?app-meeting.*?>(.*?)<'
            time = re.findall(r'%s' % (time_pattern), section)[0]
            time = time.split("-")
            start_time = convert_time_string_to_minutes(time[0].strip())
            end_time = convert_time_string_to_minutes(time[1].strip())


            location_pattern = 'location.*?>(.*?)<'
            location = re.findall(r'%s' % (location_pattern), section)[0]
            remove_digits = str.maketrans('', '', digits)
            location = location.translate(remove_digits).strip()

            day_pattern = 'day.*?>([\w]{1,2}).*?<'
            day = re.findall(r'%s' % (day_pattern), section)[0]

            return (start_time, end_time, day, location)

    print('Could not find section with CRN = %s' % (CRN))


sp2017_df = pd.read_csv('sp2017.csv')

for index, row in sp2017_df.iterrows():
    try:
        cur_info_time_day_location = get_time_day_location(str(row["CRN"]),
                                                           find_course("2017", "spring", str(row["Subject"]),
                                                                       str(row["Course"])))
        sp2017_df.at[index, "Start time"] = cur_info_time_day_location[0]
        sp2017_df.at[index, "End time"] = cur_info_time_day_location[1]
        sp2017_df.at[index, "Day"] = cur_info_time_day_location[2]
        sp2017_df.at[index, "Building"] = cur_info_time_day_location[3]
    except:
        pass

sp2017_df = sp2017_df.dropna(how='any')
sp2017_df.to_csv('sp2017_plus.csv', sep=',')
print(sp2017_df)

