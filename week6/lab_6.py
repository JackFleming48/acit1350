from scipy.stats import norm
from math import sqrt

# 1a
#P(z ≤ 2.52) 

print(str(norm.cdf(2.52, 0, 1))[:6:])

# 1b
# P(-1.06 ≤ z ≤ 2.14)

print(str(norm.cdf(2.14, 0, 1)-norm.cdf(-1.06, 0, 1))[:6:])

# 1c
# P(z ≤ -0.72

print(str(norm.cdf(-0.72, 0, 1))[:6:])

# 1d
# P(z > -2.03)

print(str(1-norm.cdf(-2.03, 0, 1))[:6:])

