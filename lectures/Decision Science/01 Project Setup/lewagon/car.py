from random import choice

class Car():
    available_colors = ['grey', 'red', 'white', 'black', 'pink']

    # Constructor
    def __init__(self, brand, color=None):
        self.color = color if color else choice(self.available_colors)
        self.brand = brand
        self.started = False

    # Car.method(arg1, [arg2]) <=> arg1.method([arg2])
    def start(self):
        print('The car is starting...')
        self.started = True

    # Class methods
    @classmethod
    def from_description(cls, description):
        # here cls = Car
        color, brand = description.split(' ')
        return cls(brand, color)

    # @classmethod
    # def other_class_method():
    #     pass

class SportsCar(Car):
    available_colors = ['red', 'white', 'yellow']

    # DRY = Don't Repeat Yourself
    def __init__(self, horsepower, brand, color=None):
        # super() calls the parent class
        super().__init__(brand, color)
        self.horsepower = horsepower











