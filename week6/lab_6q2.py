from scipy.stats import norm
from math import sqrt

# Suppose that x is a normally distributed random variable with a mean value of 97.27 and a
# standard deviation of 10.84. Determine:

# 2a
# P(x ≤ 90)

mu = 97.27
si = 10.84

print(str(norm.cdf(90, mu, si))[:6:])

# 2b
# P(100 ≤ x ≤ 120)

print(str(norm.cdf(120, mu, si)-norm.cdf(100, mu, si))[:6:])

# 2c
# P(x = 97.27)

print(0)

# 2d 
# P(x > 95)

print(str(1-norm.cdf(95, mu, si))[:6:])