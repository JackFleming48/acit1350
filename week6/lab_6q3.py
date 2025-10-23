from scipy.stats import norm
from math import sqrt

'''
A company which creates pre-packaged specialty foods is attempting to purchase a machine
which will cut and package small chunks of cheese. They would like the small packages to
fall into a weight range of 43 g to 48 g. One machine that is available will produce these
small packages with a randomly variable weight which is an approximately normally
distributed random variable with a mean of 44.9 g and a standard deviation of 1.27 g,
'''
# (a) Let X be the random variable for the package weight. Write down the expression for
# the probability that a randomly chosen package will meet the food company’s
# specification

print(str(norm.cdf((48-44.9)/1.27) - norm.cdf((43-44.9)/1.27))[:6:])

# (b) What percentage of the packages produced by this machine will not meet the food
# company’s specification?

print(1-0.9253)