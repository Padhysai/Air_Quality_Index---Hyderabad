# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:33:47 2020

@author: Sai Prasad
"""

import pandas as pd
import matplotlib.pyplot as plt


def avg_data_year(year):
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/Dependent_data/aqi{}.csv'.format(year),chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)      #Converting 24 rows to dataframe
        for index,row in df.iterrows(): #iterating all the rows in dataframe
            data.append(row['PM2.5'])   #appending 'PM2.5' row data to data
        for i in data:
            if type(i) is float or type(i) is int:      #adding int and float values to add_var
                add_var = add_var+i
            elif type(i) is str:            #if data in str format it will convert to float and add it to add_var
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var = add_var+temp
        avg = add_var/24                    #calculating avg of data
        temp_i = temp_i+1
        
        average.append(avg)
    return average
    
    
if __name__=="__main__":
    list2013 = avg_data_year(2013)
    list2014 = avg_data_year(2014)
    list2015 = avg_data_year(2015)
    list2016 = avg_data_year(2016)
    list2017 = avg_data_year(2017)
    list2018 = avg_data_year(2018)
    plt.plot(range(0,365),list2013,label="2013 data")
    plt.plot(range(0,364),list2014,label="2014 data")
    plt.plot(range(0,365),list2015,label="2015 data")
    plt.plot(range(0,365),list2016,label="2016 data")
    plt.plot(range(0,365),list2017,label="2017 data")
    plt.plot(range(0,364),list2018,label="2018 data")
    plt.show()