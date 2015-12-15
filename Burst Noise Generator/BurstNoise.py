from numpy import random

import point

	

def addBurstNoise(pointList):
	value=0
	noise=0
	count=0
	noiselevel=50
    numBits = len(pointList)
    mean = 0
    sd = 0.5
    noise = generateBurstNoise(numBits, mean, sd)

    resList = []
    for count, pt in enumerate(pointList):
        newpoint = point.Point(pt.i + noise[0][count], pt.q + noise[1][count])
        resList.append(newpoint)

    return resList


def generateBurstNoise(numBits, mean, sd):
# A count of 50000 is about 7 seconds of noise burst...
		count=0
		while count<50000:
			# Generate a random byte value.
			value=random.random(numBits)*noiselevel
			noise=value
			# Write the character, (byte), "value".
			# print(noise)
			count=count+1

    z0 = noise
    x1 = mean + z0 * sd

    return x1

#Test
seq3 = generateBurstNoise(2**6, 0, 0.5)
print(seq3)