from math import sqrt, log, sin, pi, cos
import numpy as np


# noise = np.random.normal(0, 0.5, 100)
# 0 is the mean of the normal distribution you are choosing from
# 0.5 is the standard deviation of the normal distribution
# 100 is the number of elements you get in array noise

# print(noise)

# BOX MULLER
def generate_normal(mu, sigma):
    u = np.random.random()
    v = np.random.random()

    z1 = sqrt(-2 * log(u)) * sin(2 * pi * v)
    z2 = sqrt(-2 * log(u)) * cos(2 * pi * v)

    x1 = mu + z1 * sigma
    x2 = mu + z2 * sigma

    return [x1, x2]


seq2 = [generate_normal(0, 0.5) for i in range(2 ** 8 + 16)]

print(seq2)

from numpy import random, sqrt, log, sin, cos, pi
from pylab import show, hist, subplot, figure


# transformation function
def gaussian(u1, u2):
    z1 = sqrt(-2 * log(u1)) * cos(2 * pi * u2)
    z2 = sqrt(-2 * log(u1)) * sin(2 * pi * u2)

    z1 = z1 * 0.01
    z2 = z2 * 0.01
    return z1, z2


# uniformly distributed values between 0 and 1
u1 = random.rand(1000)
u2 = random.rand(1000)

# run the transformation
z1, z2 = gaussian(u1, u2)

# plotting the values before and after the transformation
figure()
subplot(221)  # the first row of graphs
hist(u1)  # contains the histograms of u1 and u2
subplot(222)
hist(u2)
subplot(223)  # the second contains
hist(z1)  # the histograms of z1 and z2
subplot(224)
hist(z2)
show()
