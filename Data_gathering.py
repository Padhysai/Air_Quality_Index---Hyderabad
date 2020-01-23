# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:08:21 2020

@author: Sai Prasad
"""

import os
import time
import requests
import sys

def retrive_html():
    for year in range(2013,2019): #Gathering data from 2013 t0 2018
        for month in range(1,13):
            if (month<10):
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-431280.html'.format(month,year)
                
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-431280.html'.format(month,year)
              
            texts = requests.get(url)
            text_utf = texts.text.encode('utf=8')
        
            if not os.path.exists("Data/html_Data/{}".format(year)): #if path is already exist then it will add data to that path
                os.makedirs("Data/html_Data/{}".format(year))       #it will create path if not exist
            with open("Data/html_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)      
            
        sys.stdout.flush()          #Flushing all data
        
if __name__ =="__main__":
    start_time = time.time()
    retrive_html()
    stop_time = time.time()
    print("Time taken {}".format(stop_time-start_time))
    