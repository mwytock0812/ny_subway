# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 10:30:10 2014

@author: Mike
"""

#"/Users/Mike/Desktop/turnstile_data_master_with_weather.csv"

import pandas
import pandasql


def num_rainy_days(filename):
    weather_data = pandas.read_csv(filename)
    weather_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    q = """
    SELECT
    count(*)
    FROM
    weather_data
    WHERE
    cast(rain as integer) == 1
    GROUP BY
    daten;
    """
    
    #Execute your SQL command against the pandas frame
    rainy_days = pandasql.sqldf(q.lower(), locals())
    return rainy_days

def avg_min_temp(filename):
    weather_data = pandas.read_csv(filename)
    weather_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)
    
    q = """
    SELECT
    avg(cast(mintempi as integer))
    FROM
    weather_data
    WHERE
    cast(mintempi as integer) > 0 and cast(rain as integer) == 1;
    """
    
    mean_temp = pandasql.sqldf(q.lower, locals())
    return mean_temp

def avg_riders_rain(filename):
    weather_data = pandas.read_csv(filename)
    weather_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    q = """
    SELECT
    avg(ENTRIESn_hourly)
    FROM
    weather_data
    WHERE
    cast(rain as integer) == 1;
    """
    
    #Execute your SQL command against the pandas frame
    rainy_entries = pandasql.sqldf(q.lower(), locals())
    return rainy_entries

def avg_riders_no_rain(filename):
    weather_data = pandas.read_csv(filename)
    weather_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    q = """
    SELECT
    avg(ENTRIESn_hourly)
    FROM
    weather_data
    WHERE
    cast(rain as integer) == 0;
    """
    
    #Execute your SQL command against the pandas frame
    clear_entries = pandasql.sqldf(q.lower(), locals())
    return clear_entries