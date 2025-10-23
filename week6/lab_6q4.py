from scipy.stats import norm
from math import sqrt

'''
A printer manufacturer determines that the time to failure of one of their ink cartridges is
an approximately normally distributed random variable with a mean of 5570 pages and a
standard deviation of 237 pages. For marketing purposes they wish to offer a warranty to
purchasers, but to protect profitability of the company, they wish to set the warranty period
so that at most 2% of the cartridges fail under warranty. What is the longest warranty
period they can offer?
'''

mu = 5570
sig = 237
p  = 0.02

z = norm.ppf(p)

longest_warr = mu + z * sig

print(f"{str(longest_warr)[:4:]} pages")
