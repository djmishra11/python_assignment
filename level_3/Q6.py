"""

Create the custom Python classes which have methods and attributes and implement 
single inheritance, multiple inheritance, and multilevel inheritance.

"""

# Single Inheritance

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

square1 = Square(4)
print(f"Area of square is: {square1.area()}")


# Multiple Inheritance

class DC:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name + " is a DC superhero"


class Marvel:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name + " is a Marvel superhero"


class Superman(DC, Marvel):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return DC.__str__(self) + " and " + Marvel.__str__(self)

superman = Superman("Superman")
print(superman)


# Multilevel Inheritance:

class Superhero:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name + " is a superhero"

class Marvel(Superhero):
    def __init__(self, name):
        super().__init__(name)
    
    def __str__(self):
        return super().__str__() + " and a Marvel superhero"

class Hulk(Marvel):
    def __init__(self, name):
        super().__init__(name)


hulk = Hulk(name="Hulk")
print(hulk)



