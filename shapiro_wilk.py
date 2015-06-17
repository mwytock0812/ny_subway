
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 18:04:19 2014

@author: Mike
"""
import pandas
import scipy.stats
import statsmodels.api as sm
from matplotlib import pyplot as plt
import numpy as np


def shapiro_wilk(filepath, parameter):
    df = pandas.read_csv(filepath)
    array = df[parameter]
    w, p = scipy.stats.shapiro(array)
    return w, p


def shapiro_all(filepath):
    df = pandas.read_csv(filepath)
    col_names = list(df.columns.values)
    col_names = col_names[1:]
    for col in col_names:
        try:
            print col, shapiro_wilk(filepath, col)
        except:
            print col
            continue


def q_q_plot(filepath, parameter):
    df = pandas.read_csv(filepath)
    array = df[parameter]
    try:
        fig = sm.qqplot(array, scipy.stats.t, fit=True, line='45')
        plt.show()
    except:
        print "There was an error."

"""
measurements = np.random.normal(loc = 20, scale = 5, size=100000)

def qq_plot(data, sample_size):
    qq = np.ones([sample_size, 2])
    np.random.shuffle(data)
    qq[:, 0] = np.sort(data[0:sample_size])
    qq[:, 1] = np.sort(np.random.normal(size = sample_size))
    return qq

print qq_plot(measurements, 131950)
"""
