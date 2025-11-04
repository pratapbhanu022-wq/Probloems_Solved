import math
class Complex(object): 
    # object is the parent class (all Python classes inherit from it).
    '''
    This allows us to create objects like x = Complex(2, 1) representing 2+1i.
    Python already has complex numbers (2+1j), but HackerRank wants us to practice OOP
      (Object Oriented Programming) by building our own
    '''
    def __init__(self, real, imaginary): # __init__ runs when we create a new Complex number
        # complex(2,1) calls here real =2 imag=1 self.real and self.imag store these value in object
        self.real=real
        self.imaginary=imaginary
    def __add__(self, no):
        return Complex(self.real+no.real,self.imaginary+no.imaginary)
    def __sub__(self, no):
        return Complex(self.real-no.real,self.imaginary-no.imaginary)
    def __mul__(self, no):
        real_part=self.real*no.real-self.imaginary*no.imaginary
        imag_part=self.real*no.imaginary+self.imaginary*no.real
        return Complex(real_part,imag_part)
    def __truediv__(self, no):
        demon=no.real**2+no.imaginary**2
        real_part=(self.real*no.real+self.imaginary*no.imaginary)/demon
        imag_part=(self.imaginary*no.imaginary-self.real*no.imaginary)/demon
        return Complex(real_part,imag_part)
    def mod(self):
        real=math.sqrt(self.real**2+self.imaginary**2)
        return Complex(real,0)
    def __str__(self): # Special method Python calls when you do str(obj) or print(obj).
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
            '''
            use of % in this formating
            Here’s what’s happening:

"%.2f+%.2fi" → format string

%.2f → placeholder for a floating-point number with 2 decimal places

The first %.2f will be replaced by self.real

The second %.2f will be replaced by self.imaginary

% (self.real, self.imaginary) → the values to fill in the placeholders.
            '''
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (abs(self.imaginary))
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')