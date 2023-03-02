# Polymorphism means more than one form where the same entity 
# (method or operator or object) can perform different operations in different scenarios.

class Polygon:
    # method to render a shape
    def render(self):
        print("Rendering Polygon...")

class Square(Polygon):
    # renders Square
    def render(self):
        print("Rendering Square...")

class Circle(Polygon):
    # renders circle
    def render(self):
        print("Rendering Circle...")
    
# create an object of Square
s1 = Square()
s1.render()

# create an object of Circle
c1 = Circle()
c1.render()

# We have created a superclass: Polygon and two subclasses: Square and Circle.
# The render() method is defferent between the two subclasses
# Hence, the render() method behaves differently in different classes. Or, we can say render() is polymorphic.

