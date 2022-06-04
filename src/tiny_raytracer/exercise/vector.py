import math


class Vector:
    def __init__(self, *args):
        self.components = []
        for arg in args:
            self.components.append(arg)
        self.size = len(self.components)

    def __str__(self):
        return f"Components: {self.components}"

    @property
    def x(self):
        return self.components[0]

    @property
    def y(self):
        return self.components[1]

    @property
    def z(self):
        return self.components[2]

    @property
    def w(self):
        return self.components[3]

    def dot(self, other):
        result = 0
        for i in range(self.size):
            result += self[i] * other[i]

        return result

    def norm(self):
        square_sum_of_components = 0
        for c in self.components:
            square_sum_of_components += c * c
        return math.sqrt(square_sum_of_components)

    def normalize(self):
        return self / self.norm()

    def cross(self, other):
        assert self.size == 3 and other.size == 3
        return Vector(
            self.y * other.z - self.z * other.y,  # 0
            self.z * other.x - self.x * other.z,  # 1
            self.x * other.y - self.y * other.x,  # 2
        )

    def __add__(self, other):
        new_vector = []
        index = 0
        for n in self.components:
            new_vector.append(n + other.components[index])
            index += 1
        # new_vector = [1, 2, 3]
        # Vector(new_vector) => Vector([1,2,3])
        # Vector(*new_vector) => Vector(1, 2, 3)
        return Vector(*new_vector)

    def __sub__(self, other):
        return self + -other

    def __truediv__(self, divisor):
        return self * (1 / divisor)

    def __mul__(self, other):
        new_vector = []
        for n in self.components:
            new_vector.append(n * other)

        return Vector(*new_vector)

    # other * self
    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        new_vector = []
        for n in self.components:
            new_vector.append(-n)
        return Vector(*new_vector)

    def __eq__(self, other):
        for i in range(self.size):
            if self.components[i] != other.components[i]:
                return False
        return True

    def __getitem__(self, index): # vec[index]
        return self.components[index]

if __name__ == "__main__":
    print("You called this file directly")