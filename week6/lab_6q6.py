from scipy.stats import norm
from math import sqrt

'''
When X 1 and X 2 are both normally distributed random variables with means μ1 and μ 2, and
variances σ12 and σ22, respectively, their sum, X 1 + X 2 is also a normally-distributed random
variable and has the mean value μ 1 + μ2 and the variance σ12 + σ22. Suppose Hank is going
on a long trek, and he leaves with two different but fully charged cell phone batteries. Both
batteries have lifetimes (on standby) which are from populations which are approximately
normally-distributed. The first battery comes from a population with a mean of 65.24 hours
and a standard deviation of 7.42 hours, and the second battery comes from a population
with a mean lifetime of 51.22 hours and a standard deviation of 10.67 hours. Hank`s plan is
to use one battery until it dies, and then use the second one, in order to prolong his phone
usage. Compute the probability that
'''

m1 = 65.24
m2 = 51.22
s1 = 7.42
s2 = 10.67

m_total = m1 + m2
s_total = sqrt(s1**2 + s2**2)

print(f"At least 120 hrs: {str(1 - norm.cdf(120, m_total, s_total))[:6:]}")
print(f"Less than 100 hours: {str(norm.cdf(100, m_total, s_total))[:6:]}")