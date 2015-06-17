# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 17:14:22 2014

@author: Mike
"""

from pandas import *
import numpy as np
from matplotlib import pyplot as plt

def plot_weather_data(filepath):
    data = read_csv(filepath)
    x = data['Hour']
    y = data['ENTRIESn_hourly']
    
    fig = plt.figure()
    ind = np.arange(len(y))
    plt.bar(x, y)
    return plt
    
