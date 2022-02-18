from ComplexNum import ComplexNum


class ComplexCalculator:
    def add(self, a, b):
        # Takes two ComplexNum inputs and adds them together as a ComplexNum output
        return ComplexNum(a.getReal() + b.getReal(), a.getImag() + b.getImag())

    def sub(self, a, b):
        # Takes two ComplexNum inputs, a and b, and subtracts b from a
        return ComplexNum(a.getReal()-b.getReal(), a.getImag() - b.getImag())

    