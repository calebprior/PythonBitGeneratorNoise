from numpy import random, sqrt, log, sin, cos, pi
from pylab import show, hist, subplot, figure


# noise = np.random.normal(0, 0.5, 100)
# 0 is the mean of the normal distribution you are choosing from
# 0.5 is the standard deviation of the normal distribution
# 100 is the number of elements you get in array noise

# print(noise)

def generateWhiteNoise(numBits, mean, sd):
    u1 = random.random(numBits)
    v1 = random.random(numBits)

    z0, z1 = box_muller(u1, v1)

    x1 = mean + z0 * sd
    x2 = mean + z1 * sd

    return x1, x2


def box_muller(u1, v1):
    z0 = sqrt(-2 * log(u1)) * cos(2 * pi * v1)
    z1 = sqrt(-2 * log(u1)) * sin(2 * pi * v1)
    return z0, z1


#Test
seq2 = generateWhiteNoise(2**6, 0, 0.5)
print(seq2)

#Test - see what distribution looks like
u1 = random.rand(1000)
u2 = random.rand(1000)
# run the transformation
z1, z2 = box_muller(u1, u2)

figure()
subplot(221)
hist(u1)
subplot(222)
hist(u2)
subplot(223)
hist(z1)
subplot(224)
hist(z2)
show()

"""
    TODO
        Take values from mod (Point class) and add noise (above is generating two channels of noise)
        Given SNR work out sd of noise
"""
