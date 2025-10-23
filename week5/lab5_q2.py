from scipy.stats import poisson

# The number of flaws in a fiber optic cable follows
# a poisson process with an avg of 1.1 per 1000ft.

lam = 1.1*(200/1000)

print(str(poisson.pmf(2, lam))[:6:])

# The probability of exactly 1 flaw in the first 500 ft and exactly 2 in the second 500ft

lam = 1.1*(500/1000)
first5 = poisson.pmf(1, lam)
secondn5 = poisson.pmf(2, lam)
print(str(first5*secondn5)[:6:])

# The probability of betweem 5 and 10 flaws (inclusive) in a 5000-foot cable

lam = 1.1*5

print(str(poisson.cdf(10, lam)-poisson.cdf(4, lam))[:6:])