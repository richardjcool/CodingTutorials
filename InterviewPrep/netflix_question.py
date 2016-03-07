"""Create a simple data set that lets me solve my Netflix problem using
Pandas. During the interview, I solved it using simple reading of the csv file.
Pandas probably is better."""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import math

def create_data_set():
    Npoint = 1000
    mean = 200.
    sigma = 50.
    date0 = 0
    twindow = 365

    date = pd.Series(map(int, np.random.rand(Npoint)*twindow + date0),
                     name='Date')
    nstream = pd.Series(np.random.randn(Npoint)*sigma+mean, name='nstream')

    df = pd.concat([date, nstream], axis=1)
    df.to_csv('/Users/rcool/CodingTutorials/InterviewPrep/netflix.csv')


def running_average(df):

    runningAv = []
    for date in df.loc[:, 'Date']:
        streams = [y for x, y in zip(df.loc[:, 'Date'], df.loc[:, 'nstream'])
                   if np.abs(date-x) < 14]
        runningAv.append(sum(streams)/len(streams))
    return runningAv

if __name__ == '__main__':

    filename = '/Users/rcool/CodingTutorials/InterviewPrep/netflix.csv'
    if os.path.isfile(filename) is False:
        create_data_set()

    df = pd.read_csv(filename)
    av = running_average(df)

    # plt.hist(df.loc[:, 'nstream'], math.floor(365/14), facecolor='magenta')
    plt.scatter(df['Date'], df['nstream'], c='black')
    plt.scatter(df.loc[:,'Date'], av, c='blue')
    plt.show()
