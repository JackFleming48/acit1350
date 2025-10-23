from scipy.stats import poisson

# The probability that 2 jobs will arrive at any given minute

lam = 0.4
print(str(poisson.pmf(2, lam))[:6:])

# The probability that at most 3 jobs will arrive during a 5 minute interval

lam = 0.4*5

print(str(poisson.cdf(3, lam))[:6:])

# The probability that atleast 3 jobs will arrive in a 2 minute interval

lam = 0.4*2

print(str(1-poisson.cdf(2, lam))[:6:])

