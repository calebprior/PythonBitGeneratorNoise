#!/usr/bin/env python
# -*-coding:utf-8-*-
#
# A simple, high level, implementation of a LFSR.
#
# Fibonacci model
#
#   __________+_______+________________
#  |          ^       ^                ^
#  |     ___  |  ___  |  ___     ___   |
#  |    |   | | |   | | |   |   |   |  |
#  ---->| d |---| c |---| b |---| a |------> S = ..., s_1, s_0
#       |___|   |___|   |___|   |___|
#         3       2       1       0
#
#   ______+___+_______
#  |      ^   ^       ^
#  |     _|_ _|_ ___ _|_
#  |    |   |   |   |   |
#  ---->| d | c | b | a |------> S = ..., s_1, s_0
#       |___|___|___|___|
#         3   2   1   0
#
# $ python
# Python 2.6.2 (release26-maint, Apr 19 2009, 01:56:41)
# [GCC 4.3.3] on linux2
# Type "help", "copyright", "credits" or "license" for more information.

# >>> x = LFSR([0,0,1,0,1], [1,0,0,1,1])
# >>> x.dump()
# ([0, 0, 1, 0, 1], [1, 0, 0, 1, 1])
# >>> x.period()
# 7
# >>> x.clock()
# 0
# >>> x.clock()
# 0
# >>> x.clock()
# 1
# >>> x.clock()
# 0
# >>> x.clock()
# 1
# >>> x.clock()
# 1
# >>> x.clock()
# 0
# >>> x.clock()
# 0
# >>> x.clock()
# 0
# >>> x.clock()
# 1
#
# Copyright (c) Stefan Pettersson 2007, http://www.bigpointyteeth.se/
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
from functools import reduce


class LFSR(object):
    def __init__(self, seed, feedback):
        """Returns a linear feedback shift register with seed as the initial
		values and feedback as the feedback polynomial.

		>>> x = LFSR([0,0,0,1], [1,0,1,0])

		The feedback polynomial given above, 1 + x^2, is primitive and will
		generate the maximum possible sequence of length 2^4 - 1 = 15."""
        self.length = len(seed)
        self.clocks = 1
        self.seed = seed[:]
        self.register = seed
        self.feedback = feedback
        # at which indices do we have taps?
        self.taps = []
        for i in range(len(feedback)):
            if feedback[i]: self.taps.append(i)

    def _xor(self, a, b):
        """Helper function that returns the sum mod 2 of a and b."""
        return a ^ b

    def period(self):
        """Returns the period of the LFSR."""
        tmp = self.register[:]
        clocks = 1
        self.clock(False)  # cheap one, i know, bit there are no do loops
        while self.register != tmp:
            self.clock(False)
            clocks += 1
        return clocks

    def dump(self):
        """Print the LFSRs current register and its feedback polynomial."""
        return self.register, self.feedback

    def clock(self, count = True):
        """Clock one step of the LFSR and return the popped value."""
        # prevent from incrementing the counter when used internally, like period()
        if count: self.clocks += 1
        add = reduce(self._xor, [self.register[i] for i in self.taps])
        self.register.append(add)
        pop = self.register.pop(0)
        return pop

        # EOF


x = LFSR([1, 1, 0, 1], [1, 1, 0, 1])

seq = [x.clock() for i in range(2 ** 16 + 16)]

print(seq)
