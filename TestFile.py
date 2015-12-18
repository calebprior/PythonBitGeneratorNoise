from pylab import show, hist, subplot, figure
from numpy import random

import BitGen
import WhiteNoiseGenerator
import BurstNoise

# Test Bit Gen

testBitGen = BitGen.generateBitSequence(100, 1)
print(testBitGen)

#Test White Noise
testWhiteNoise = WhiteNoiseGenerator.generateWhiteNoise(2 ** 6, 0, 0.5)
print(testWhiteNoise)


#Test - see what distribution looks like
u1 = random.rand(1000)
u2 = random.rand(1000)
# run the transformation
z1, z2 = WhiteNoiseGenerator.box_muller(u1, u2)

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