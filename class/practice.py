import math

class Complex(object):
    def init(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def sub(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def mul(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def truediv(self, other):
        denom = other.real2 + other.imag2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real, imag)

    def mod(self):
        magnitude = math.sqrt(self.real2 + self.imag2)
        return Complex(magnitude, 0)

    def __str__(self):
    # Round to 2 decimals first
        r = round(self.real, 2)
        i = round(self.imaginary, 2)

    # Normalize tiny values to 0.0 to avoid '-0.00'
        if abs(r) < 0.005: r = 0.0
        if abs(i) < 0.005: i = 0.0

        sign = '+' if i >= 0 else '-'
        return f"{r:.2f}{sign}{abs(i):.2f}i"


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')