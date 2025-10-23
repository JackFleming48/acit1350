from scipy.stats import binom
from math import sqrt

# a. probability that exactly 94 of the adults will have diabetes

x = 94
p = 0.094
n = 1000
q = 1 - 0.094

print(str(binom.pmf(x, n, p))[:6:])

# b. probability that more than 80 will have diabetes

x = 80

print(str(1-binom.cdf(x, n, p))[:6:])

# c. probability that not more than 65 will have diabetes

x = 65

print(str(binom.cdf(x, n, p))[:6:])

# d. probability that fewer than 100 will have diabetes

x = 99

print(str(binom.cdf(x, n, p))[:6:])

# e. probability that at least 75 will have it

x = 74

print(str(1-binom.cdf(x, n, p))[:6:])

# f. probability that fewer than 20 will have diabetes

x = 19

print(str(binom.cdf(x, n, p)))

# g. probability that between 50 and 90 (inclusive) will have diabetes

x = 90

print(str(binom.cdf(x, n, p)-binom.cdf(50, n, p))[:6:])

# h. Suppose that of the 1000 tested only 32 were found to have type 2 diabetes. What
# conclusions might you make? Answer by finding the appropriate probability. Calculate it
# and enter it on your worksheet

np = n*p
nq = n*q
npq = sqrt(n*p*q)
is_unusual = False

if np >= 5 and nq >= 5:
    z = (32-np)/npq

    if not (2 > z > -2):
        is_unusual = True

print(f"{is_unusual} it is unusual")

# i. calculate the mean

print(np)

# calculate std deviation

std_dev = sqrt(n*p*(1-p))

print(str(std_dev)[:6:])

