from scipy.stats import norm
from math import ceil

'''
Consider the following problem:
A technologist recruited a random sample of 35 students at a major educational
institution, and tracked the time each spent with their smartphones active during a
randomly selected 24-hour period. This sample had a mean of 125.62 minutes. Suppose it
is know that the population of times is normally distributed with standard deviation σ =
30.3 minutes. Construct a 98% confidence interval estimate of the true mean minutes that
the smartphones of students are active over a 24-hour period
'''

# 2. Compute the value of 𝑧 alpha/2. You will need to use the norm.ppf function with the appropriate
# values. Enter this value in the appropriate place in your Word document

alph = 0.02
sigma = 30.3
xbar = 125.62
n = 35
zalpha_overtwo = 0.01

print(f"the 98th percentile is {norm.ppf(1-zalpha_overtwo)}")

# 3. Compute the appropriate value of 𝜎𝜎𝑥𝑥̅. Enter this value in the appropriate place in your Word
# document

from math import sqrt

sigma_xbar = sigma / sqrt(n)

print(f"sigma of xbar is: {sigma_xbar}") 

# 4. Compute the endpoints of the confidence interval using your values from the previous steps.
# Put the confidence interval in the appropriate place in your Word document. Make sure to put
# your confidence interval in one of the standard forms.
z_value = norm.ppf(1-zalpha_overtwo)
big_e = z_value*sigma_xbar

lower = xbar - big_e
upper = xbar + big_e

print(f"The CI is: ({lower}, {upper})")

'''
Consider the following problem:
A technologist recruited a random sample of 35 students at a major educational
institution, and tracked the time each spent with their smartphones active during a
randomly selected 24-hour period. This sample had a mean of 125.62 minutes and a
standard deviation of 30.3 minutes. Suppose it is know that the population of times is
normally distributed, but the standard deviation is unknown. Construct a 98% confidence
interval estimate of the true mean minutes that the smartphones of students are active
over a 24-hour period.
'''

# 6. Compute the value of 𝑡𝑡𝛼𝛼/2. You will need to use the t.ppf function with the appropriate
# values. Enter this value in the appropriate place in your Word document

n = 35
df = 35 - 1
xbar = 125.62
alph = 0.02
talpha_overtwo = 0.02 / 2
s = 30.3

from scipy.stats import t

t_value = t.ppf(1-talpha_overtwo, df)

print(f"the t value is: {t_value}")

# 7. Compute the appropriate value of 𝜎𝜎𝑥𝑥̅. Enter this value in the appropriate place in your Word
# document.

s_xbar = s / sqrt(n)

print(f"the value of s xbar is: {s_xbar}")

# 8. Compute the endpoints of the confidence interval using your values from the previous steps.
# Put the confidence interval in the appropriate place in your Word document. Make sure to put
# your confidence interval in one of the standard forms

big_e = t_value * s_xbar

upper = xbar + big_e
lower = xbar - big_e

print(f"The CI is: ({lower}, {upper})")

'''
Consider the following problem:
A random sample of 80 chips from a potential supplier are tested, and 71 are found to meet a
company's specifications.
'''

# 10. Construct a 90% confidence level estimate of the true proportion of the chips from this
# supplier which will meet the company’s specifications. Copy this confidence interval to the
# appropriate place in your Word document.

n = 80
x = 71

p = x / n

sigma_p = sqrt((p*(1 - p)) / n)

zalpha_overtwo = 0.05
z_value = norm.ppf(1-zalpha_overtwo)

big_e = z_value * sigma_p

np = n*p
also = n*(1 - p)

if np >= 5 and also >= 5:
    lower = p - big_e
    upper = p + big_e
    print(f"The CI of the true proportion of chips is: ({lower}, {upper})")

'''
PEN AND PAPER PROBLEMS (CODE)
'''

t_value = t.ppf(1-0.025, 34)
print(f"The t value is: {t_value}")

big_e = 2.032244509317718 * (0.65 / sqrt(35))
print(f"The big e is: {big_e}")

print(f"The CI is: ({31.3 - big_e}, {31.3 + big_e})")

n = 140
x = 113
p = x / n
sigma_p = sqrt((p * (1 - p)) / n)
zalpha_overtwo = 0.025
z_value = norm.ppf(1-zalpha_overtwo)
print(f"The z val is : {z_value}")
np = n*p
also = n*(1-p)
print(f"The np: {np}\nThe also: {also}")
big_e = z_value*sigma_p
print(f"the big e is: {big_e}")
lower = p - big_e
upper = p + big_e
print(f"the range is ({1-lower}, {1-upper})")

n = 140
xbar = 101.23
s = 13.88
df = 139
talpha_overtwo = 0.025
t_value = t.ppf(1 - talpha_overtwo, df)
print(f"The t value is: {t_value}")
s_xbar = s / sqrt(n)
print(f"s xbar is: {s_xbar}")
big_e = s_xbar*t_value
print(f"The big e is: {big_e}")
lower = xbar - big_e
upper = xbar + big_e
print(f"The CI is: ({lower}, {upper})")


print(t.ppf(1-0.025, 14))
big_e = 2.1448 * (s / sqrt(n))
print(big_e)
xbar = 9.26
lower = xbar - big_e
upper = xbar + big_e
print(f"The CI is: ({lower}, {upper})")
print(((2.5160*3.67)/1)**2)