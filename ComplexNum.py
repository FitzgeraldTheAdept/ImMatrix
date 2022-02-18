import math


class ComplexNum:
    def __init__(self, re, im):
        self.real = re
        self.imag = im

    def getReal(self):
        return self.real

    def getImag(self):
        return self.imag

    def arg(self):
        # returns the angle of this imaginary number in the imaginary plane
        val = math.atan(self.imag / self.real)

        if self.real < 0:
            # In quadrants 2 or 3
            return -val
        else:
            # In quadrants 1 or 4
            return val

    def abs(self):
        # return the absolute value of the number
        return math.sqrt(math.pow(self.real, 2) + pow(self.imag, 2))

    def torect(self):
        # return a string format of this number in rectangular form
        if self.imag < 0:
            # negative i format
            return '%f - i%f' % (self.real, math.fabs(self.imag))
        else:
            # positive i format
            return '%f + i%f' % (self.real, self.imag)

    def topolar(self):
        # return a string format of this number in polar form
        return '%f e^(i %f)' % (self.abs(), self.arg())

    def topolardeg(self):
        # return a string format of this number in polar form in degrees
        return '%f e^(i %f)' % (self.abs(), self.arg() * (180 / math.pi))

    # Iterable Object Stuff
    def __iter__(self):
        return self

    def __next__(self):
        return self
