from numpy import random, sqrt, log, sin, cos, pi
from pylab import show, hist, subplot, figure

import point

def sdForSnrValue(SNR):
    sd = sqrt((1 / SNR))

    return sd

def addWhiteNoise(pointList, SNR):
    numBits = len(pointList)
    mean = 0
    sd = sdForSnrValue(SNR)
    noise = generateWhiteNoise(numBits, mean, sd)

    resList = []
    for count, pt in enumerate(pointList):
        newpoint = point.Point(pt.i + noise[0][count], pt.q + noise[1][count])
        resList.append(newpoint)

    return resList


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

"""
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
"""
    TODO
        Given SNR work out sd of noise
"""

