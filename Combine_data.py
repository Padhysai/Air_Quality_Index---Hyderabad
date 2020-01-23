# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 16:27:09 2020

@author: Sai Prasad
"""

from Data_gathering_2 import avg_data_year
import requests
import sys
import pandas as pd
import os
import csv
from bs4 import BeautifulSoup

def meta_data(month, year):
    
    file_html = open('Data/html_Data/{}/{}.html'.format(year,month), 'rb')
    plain_text = file_html.read()

    tempD = []
    finalD = []

    soup = BeautifulSoup(plain_text, "lxml")
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):      #Finding the data from tabel in html
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempD.append(a)

    rows = len(tempD) / 15          #Dividing data into row wise, we have 15 features

    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)

    length = len(finalD)

    finalD.pop(length - 1)
    finalD.pop(0)

    for a in range(len(finalD)):
        finalD[a].pop(6)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(9)
        finalD[a].pop(0)

    return finalD

def data_combine(year, cs):
    for a in pd.read_csv('Data/Combined-Data/combined_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist



if __name__=="__main__":
    if not os.path.exists("Data/Combined-Data"):
        os.makedirs("Data/Combined-Data")
    
    for year in range(2013,2019):
        final_data = []
        with open('Data/Combined-Data/combined_'+str(year)+'.csv','w') as csvfile:   #Creating csv files for each year
            wr = csv.writer(csvfile,dialect='excel')
            wr.writerow(['T','TM','Tm','SLP','H','W','V','VM','PM2.5'])     #creating columns
        for month in range(1,13):
            temp = meta_data(month,year)
            final_data = final_data + temp
            
        pm = avg_data_year(year)            #Dependent feature
        
        if len(pm)==364:
            pm.insert(364,'-')
            
        for i in range(len(final_data)-1):
            final_data[i].insert(8,pm[i])       #Inserting pm value in 8th column,i.e.,PM2.5
    
        with open('Data/Combined-Data/combined_'+str(year)+'.csv','a') as csvfile:          #append mode
            wr = csv.writer(csvfile,dialect='excel')
            for row in final_data:
                flag=0
                for elem in row:
                    if elem =="" or elem =="-":
                        flag=1
                if flag!=1:
                    wr.writerow(row)
                    
    data_2013 = data_combine(2013,600)
    data_2014 = data_combine(2014,600)
    data_2015 = data_combine(2015,600)
    data_2016 = data_combine(2016,600)
    data_2017 = data_combine(2017,600)
    data_2018 = data_combine(2018,600)
    
    total = data_2013+data_2014+data_2015+data_2016+data_2017+data_2018
    
    with open('Data/Combined-Data/Original_data.csv','w') as csvfile:
        wr = csv.writer(csvfile,dialect='excel')
        wr.writerow(['T','TM','Tm','SLP','H','W','V','VM','PM2.5'])
        wr.writerows(total)
        
df = pd.read_csv('Data/Combined-Data/Original_data.csv')
            