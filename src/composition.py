class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power


class Wheel:
    def __init__(self, wheel_size):
        self.wheel_size = wheel_size


class Chassis:
    def __init__(self, color):
        self.color = color


class Car:
    def __init__(self, engine, wheels, chassis):
        self.engine = engine
        if len(wheels) != 4:
            print("Error: A car should have 4 wheels")
        self.wheels = wheels
        self.chassis = chassis

    def __str__(self):
        return f"The car has {self.engine.horse_power} horse power, a {self.chassis.color} color and {len(self.wheels)} wheels with size {self.wheels[0].wheel_size}"

    def top_speed(self):
        # do some calculation based on horse power
        # wheel size
        return 200


engine = Engine(200)
wheels = [Wheel(20)] * 4
chassis = Chassis("red")
car = Car(engine, wheels, chassis)


print(car)
