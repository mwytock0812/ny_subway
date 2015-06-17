# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 11:48:42 2014

@author: Mike
"""

import numpy as np
import pandas
import matplotlib.pyplot as plt

def entries_histogram(filepath):
    weather_data = pandas.read_csv(filepath)
    rainy = weather_data['ENTRIESn_hourly'][weather_data['rain']==1]
    clear = weather_data['ENTRIESn_hourly'][weather_data['rain']==0]  
    plt.figure()
    rainy.hist(bins=100, color = 'b', alpha = 0.5, label='Rainy Days')
    clear.hist(bins=100, color = 'g', alpha = 0.5, label='Clear Days')
    legend()
    plt.xlabel('Number of Hourly Entries')
    plt.ylabel('Frequency of Entries by Presence of Rain')
    plt.xlim(0, 20000)
    return plt