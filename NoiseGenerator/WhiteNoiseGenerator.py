from numpy import random, sqrt, log, sin, cos, pi
import point

def sdForSnrValue(SNRdb):
    SNRlin = 10**(SNRdb / 10)
    variance = 1.0 / sqrt(SNRlin)
    sd = sqrt(variance)
    return sd

print(sdForSnrValue(10))
print(sdForSnrValue(4))
print(sdForSnrValue(6))
print(sdForSnrValue(40))

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

