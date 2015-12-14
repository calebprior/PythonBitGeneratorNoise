from operator import xor
from functools import reduce


def lfsr(coefficients, state=[]):
    """
        This implements a LFSR. The inputs are the 'coefficients'
        of the feedback function and the initial 'state' of the
        register.
    """
    # If state is longer than coefficients, truncate it.
    # If state is shorter than coefficients, pad it with 1s.

    m = len(coefficients)
    state = state[:m]
    state = state + [1]*(m-len(state))

    while 1:
        state.append(dot(coefficients,state))
        yield state.pop(0)

def dot(x,y):
    """ This returns the 'dot' product of the two binary lists
        'x' and 'y'. If either list is empty '0' is returned.
    """
    return reduce(xor, [a & b for (a, b) in zip(x, y)], 0)


class Poly(list):
    """
        A class for polynomials. The coefficients are
        stored as a list [c0, c1, ... , c_m] where the polynomial
        is c0*x**m + c1*x**(m-1) + ... + c{m-1}*x + c_m.

        Class provides a means of printing the stored list

        For example:
        Poly([1,0,1,0]) => x^3 + x^1
    """

    def __str__(self):
        L = ["x^%s" % (k,) for (k, x) in enumerate(self[::-1]) if x == 1 ]
        L.reverse()
        return "+".join(L)


X = Poly([1, 0, 1, 0])
testS = [1, 1, 0, 1]

bitgen = lfsr(X, testS)

seq = [bitgen.__next__() for i in range(2 ** 16 + 16)]

print(seq)
print(X)
