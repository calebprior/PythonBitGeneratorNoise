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
        L = [" x^%s " % (k,) for (k, x) in enumerate(self[::-1]) if x == 1 and k != 0]
        L.reverse()
        return "+".join(L) + "+ " + str(self.__getitem__(self.__len__() - 1))

