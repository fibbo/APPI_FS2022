class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        return Complex(new_real, new_imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


c1 = Complex(4, 3)
c2 = Complex(-1, -7)

print(c1 + c2)