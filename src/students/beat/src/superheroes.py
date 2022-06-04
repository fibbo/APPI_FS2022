class Mutant:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def info(self):
        print(f"I'm an abstract mutant, my name is {self.name} and I'm {self.gender}.")

    def superpower(self):
        print("I'm abstract, I don't have any superpowers.")


class Superhero(Mutant):
    def __init__(self, name, gender, superpower):
        super().__init__(name, gender)
        self.superpower = superpower

    def info(self):
        print(
            f"I'm {self.name}, I'm a {self.gender} mutant and my power is: {self.superpower}."
        )

    def classified(self):
        print("Classification: Superhero")


class Supervillain(Mutant):
    def __init__(self, name, gender, crimes):
        super().__init__(name, gender)
        self.crimes = crimes

    def info(self):
        print(
            f"I'm {self.name}, I'm a {self.gender} mutant and I'm accused for: {self.crimes}."
        )

    def classified(self):
        print("Classification: Supervillain")


list_of_mutant = [
    Superhero("Superman", "male", "Superstrength"),
    Superhero("Wonderwoman", "female", "Superspeed"),
    Supervillain("Joker", "male", "Robbery"),
]
for mutant in list_of_mutant:
    mutant.info()
    mutant.classified()
