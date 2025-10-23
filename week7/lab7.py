from scipy.stats import norm
from math import sqrt
'''
The lifetimes of a certain brand of tire are normally distributed with mu=30_000 and sigma=4500
'''

#1a - P(A tire lasts longer than 31_000)

print(str(1 - norm.cdf(31000, 30000, 4500))[:6:])

#1b - P(Life time of 40 tires is > 31_000)

print(str(1 - norm.cdf(31000, 30000, 711.5124735))[:6:])

#1c - P(Life time of 500 tires is > 31_000)

print(str(1 - norm.cdf(31000, 30000, 201.246118)))

'''
2.
The tensile strength of a plastic bag has mu=2900psi and sigma=26psi.
If you purchase 50 of these bags what is P(tensile strength < 2890psi)
'''

print(str(1 - norm.cdf(2890, 2900, 3.676955262))[:6:])

'''
3.
CIT grad incomes have a mu=50_000 and sigma=6000. If 12 grads are slected, P(income > 55_000)
'''

print(str(1 - norm.cdf(55000, 50000, 1732.050808))[:6:])

'''
4.
A copper sites copper concentration has mu=65ppm and sigma=5ppm
'''

#4a - n=25, probability that xbar is between 64 and 67? atleast 68?

xbarsig = 5 / sqrt(25)

# between 67 and 64
print(str(norm.cdf(67,65,xbarsig)-norm.cdf(64,65,xbarsig))[:6:])
# atleast 68
print(str(1-norm.cdf(68,65,xbarsig))[:6:])


#4b - n=100

xbarsig = 5 / sqrt(100)

# between 67 and 64
print(str(norm.cdf(67,65,xbarsig)-norm.cdf(64,65,xbarsig))[:6:])
# atleast 68
print(str(1-norm.cdf(68,65,xbarsig)))


'''
Ulnar nerve motor mu=45m/s, sigma=7m/s, n=40, P(X < 43.5)
'''

xbarsig = 7 / sqrt(40)

print(str(norm.cdf(43.5, 45, xbarsig))[:6:])