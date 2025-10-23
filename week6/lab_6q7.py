from scipy.stats import lognorm
from math import exp

'''
When software system crashes occur, it is often the case that
T, the time to system restoration, is a random variable, and
that it is log eT = ln T which is approximately normally
distributed. When ln T has a normal distribution, we say that
T itself has a lognormal distribution. The probability density
function for T is shown to the right.
Suppose that historical records indicate that the time T (in
minutes) to restoration of service of a learning management
system after a system crash is known to be lognormally-
distributed with the mean and standard deviation of the values of ln T being 5.168 and 1.23
respectively.
'''

m = 5.168
sig = 1.23
dst = lognorm(s=sig, scale=exp(m))

l_115 = dst.cdf(115)
g_3 = 1-dst.cdf(180)

print(f"Less than 150: {str(l_115)[:6:]}")
print(f"Greater than 3 hours: {str(g_3)[:6:]}")