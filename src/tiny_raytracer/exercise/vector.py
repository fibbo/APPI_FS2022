import math


class Vector:
    # TODO: Implement constructor
    def __init__(self, *args):
        self.components = []
        for arg in args:
            self.components.append(arg)
        self.size = len(self.components)

    # TODO: Implement __str__

    # TODO: Implement properties
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

    # TODO: Implement dot product

    def norm(self):
        square_sum_of_components = 0
        for c in self.components:
            square_sum_of_components += c * c
        return math.sqrt(square_sum_of_components)

    # TODO: Implement normalize

    # TODO: Implement cross product
    def cross(self, other):
        assert self.size == 3 and other.size == 3
        return Vector(
            self.y * other.z - self.z * other.y, # 0
            self.z * other.x - self.x * other.z, # 1
            self.x * other.y - self.y * other.x  # 2
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


    # TODO: Implement __sub__ (subtraction)

    # TODO: Implement division (which special function name is the correct one?)

    # TODO: Implement __mul__ (multiplication)

    # TODO: Try vector * scalar and scalar * vector

    # TODO: Implement __neg__ (additive inverse)

    def __eq__(self, other):
        for i in range(self.size):
            if self.components[i] != other.components[i]:
                return False
        return True

    # TODO: Implement __getitem__

    pass
