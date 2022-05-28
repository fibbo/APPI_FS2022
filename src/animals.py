class Animal:
    def __init__(self, weight):
        self.weight = weight

    def info(self):
        print(f"I'm an abstract animal and I don't have a concept of weight.")

    def noise(self):
        print("I'm abstract, I don't make noises. Or maybe abstract noises...")


class Mammal(Animal):
    def __init__(self, weight):
        super().__init__(weight)
    
    def info(self):
        print(f"Abstract mammal")


class Cat(Mammal):
    def __init__(self, weight, color):
        super().__init__(weight)
        self.color = color

    def info(self):
        Animal.info(self)
        print(f"I'm a {self.color} cat that weighs {self.weight} kg.")

    def noise(self):
        print("Meow")

my_cat = Cat(5, "white")
my_cat.noise()
my_cat.info()


class Dog(Animal):
    def __init__(self, weight, breed):
        super().__init__(weight)
        self.breed = breed

    def info(self):
        print(f"I'm a {self.breed} dog that weighs {self.weight} kg.")

    def noise(self):
        print("Woof!")


# cat = Cat(6, "Red")