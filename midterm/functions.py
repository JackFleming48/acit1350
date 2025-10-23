import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV data
s1 = pd.read_csv(
    'file_to_read.txt',
    sep='\t', # what seperates the lines
    skiprows = 3 # how many rows from top to skip
)

# Create Histogram
def create_histogram(s1):
    plt.figure(figsize=(12,5)) #width,height in inches
    plt.subplot(1,2,1) # add axes to current figure
    sns.histplot(s1['some_attribute'], bins=20) # bins -> how many intervals or bars the data is divided into
    plt.title('What we are plotting')
    plt.xlabel('Label X axis')

# Another Histogram

plt.hist(
    s1['some_attribute'],
        bins=10, 
        weights=np.ones_like(s1['some_attribute']) / len(s1['some_attribute'])*100,
        color='skyblue',
        edgecolor='black'
    )
plt.title('Percent Frequency Histogram of Score')
plt.xlabel('Score')
plt.ylabel('Percent')
plt.show()

# Compute mean
mean = s1['some_attribute'].mean()
print(mean)

# Compute median
median = s1['some_attribute'].median()

# Compute std_dev
sigma = s1['some_attribute'].std()

# Compute variance
var = s1['some_attribute'].var()

# Compute range
rge = s1['some_attribute'].max() - s1['some_attribute'].min()

# Interquartile/quantile
def intquart(s1):
    q_one = s1.quantile(0.25)
    q_three = s1.quantile(0.75)

    return q_three - q_one

# Side by side graph
def side_by_side(set1, set2):
    bins = range(30, 81, 5)

    plt.hist([set1, set2], bins=bins, 
             label=['Set 1', 'Set 2'], 
             edgecolor='black', 
             alpha=0.7, 
             histtype='bar', 
             rwidth=0.9)

    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.title('Set 1 vs. Set 2')
    plt.legend()
    plt.show()

# Boxplot
sns.boxplot(x='set', y='score', data=s1)
plt.title('Boxplot title')
plt.show()

# create one-dimenstional labeled array in pandas to store sequence of data
s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(s)

'''
!!!binom!!!
'''

from scipy.stats import binom
from math import sqrt

# binom.pmf : calculates the probability mass function for a binomial distribution
# the probability of getting exactly k successes in n independent trials, when each trial has success p
# k is inclusive
k, n ,p = 0
binom.pmf(k, n, p)

# binom.cdf : the probability of getting k or fewer successes in n independant trials with probability p
binom.cdf(k, n, p)

# 1-binom.cdf : the probability of getting more than k succeses
1-binom.cdf(k, n, p)

# binom.cdf-binom.cdf : probabilty that a range of k
binom.cdf(k, n, p)-binom.cdf(k, n, p)

# some binom values
# n = number of trials
# p = probability of success
# q = 1 - p : probability of failure
q = 1-p
expected_number_of_failures = n*q
std_dev = sqrt(n*p*q)
variance = n*p*q
mean = n*p

'''
!!!POISSON!!!
'''

from scipy.stats import poisson

# Poisson distribution models the number of times an event occurs in a fixed interval of time or space

# mu (poisson lambda)
rate, interval, k = 0
lam = rate * interval

# poisson.pmf(k, lam) : the probability of observing exactly k events, given an avg rate lam
poisson.pmf(k, lam)

# poisson.cdf(k, lam) : the probability of observing k or fewer events
poisson.cdf(k, lam)

# 1-poisson.cdf(k, lam) : More than k events
1-poisson.cdf(k, lam)

# poisson.cdf(k, lam)-poisson.cdf(k, lam) : the probability that x is between two values
poisson.cdf(k, lam)-poisson.cdf(k, lam)

'''
!!!NORM!!!
'''

from scipy.stats import norm
from math import sqrt

# The probability that a normally distributed random variable is less than or equal to a given value x
# tells you P(X <= x)

# norm.cdf(x, mean, std_dev)
x, mean, std_dev = 0
norm.cdf(x, mean, std_dev)
1-norm.cdf(x, mean, std_dev)

# norm.cdf(x, mean, std_dev)-norm.cdf(x, mean, std_dev) a range
norm.cdf(x, mean, std_dev)-norm.cdf(x, mean, std_dev)

# norm.ppf(p) : find the z-score for a probability (area to left)
norm.ppf(p) 