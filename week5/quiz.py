from scipy.stats import binom, poisson
# exactly 10 households user solar panels

x = 10
p = .30
n = 20

print(binom.pmf(x, n, p))

# atleast 6 houses use

x = 5

print(1-binom.cdf(x,n,p))

# fewer than 4 houses use

x = 3
print(binom.cdf(x,n,p))

# q2

lam = .3*3
print(1-poisson.cdf(9,lam))