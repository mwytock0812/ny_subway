# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 14:19:08 2014

@author: Mike
"""
#"turnstile_data_master_with_weather.csv"

import numpy as np
import pandas
import scipy
import matplotlib.pyplot as plt


def normalize_features(array):
    """
    Normalize the features in our data set.
    """
    mu = array.mean()
    sigma = array.std()
    array_normalized = (array-mu)/sigma
    return array_normalized, mu, sigma


def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, and the values for our thetas.
    """
    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)
    return cost


def gradient_descent(features, values, theta, alpha, num_iterations):
    m = len(values)
    cost_history = []

    for i in range(num_iterations):
        predicted_values = np.dot(features, theta)
        theta = theta - alpha/m * np.dot((predicted_values - values), features)
        cost = compute_cost(features, values, theta)
    return theta, pandas.Series(cost_history)


def predictions(filepath):
    dataframe = pandas.read_csv(filepath)
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = dataframe[['rain']].join(dummy_units)
    values = dataframe[['ENTRIESn_hourly']]
    m = len(values)

    features, mu, sigma = normalize_features(features)

    features['ones'] = np.ones(m)
    features_array = np.array(features)
    values_array = np.array(values).flatten()

    #Set values for alpha, number of iterations.
    alpha = 0.1 # please feel free to play with this value
    num_iterations = 75 # please feel free to play with this value

    #Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array, values_array, theta_gradient_descent,
                                                            alpha, num_iterations)

    predictions = np.dot(features_array, theta_gradient_descent)

    return predictions


def plot_residuals(filepath, predictions):
    turnstile_weather = pandas.read_csv(filepath)
    plt.figure()
    (turnstile_weather['ENTRIESn_hourly'] - predictions).hist(bins=100)
    plt.title('Histogram of Residuals for Rain as the Only Regression Feature')

    plt.xlabel('Residuals for Regression Model')
    plt.ylabel('Frequency of Occurrence for Given Residuals')
    plt.xlim(-12500, 15000)
    return plt
