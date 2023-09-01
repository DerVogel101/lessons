# Author: DerVogel101
# Description: A simple circle class with some basic functions
# Date: 01.09.2023
# Task:
# Create a Circle class.
# - The constructor should receive a center point and a radius.
# - A method should return the circumference of the circle.
# - A method should return the area of the circle.
# - A method should increase the radius by a factor.
# - Additional: The distance between two circles' outer edges should be able to be calculated.

import math


class Circle:
    def __init__(self, cordinate: list[int, int], radius):
        self.cordinate = cordinate
        self.radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def size_multiplier(self, multiplier):
        self.radius *= multiplier

    def distance(self, circle2):
        return math.sqrt((circle2.cordinate[0]-self.cordinate[0])**2 + (circle2.cordinate[1]-self.cordinate[1])**2) - (circle2.radius + self.radius)


if __name__ == "__main__":
    my_circle: Circle = Circle([20, 20], 5)
    print(f"Umfang: {my_circle.get_circumference()}")
    print(f"Fläche: {my_circle.get_area()}")
    my_circle.size_multiplier((r_mul := 2))
    print(f"Radius um den faktor {r_mul} vergrößert")
    print(f"Umfang: {my_circle.get_circumference()}")
    print(f"Fläche: {my_circle.get_area()}")
    print(f"Koordinaten: {my_circle.cordinate}")

    my_circle2: Circle = Circle([0, 0], 5)
    print(f"Entfernung: {my_circle.distance(my_circle2)}")
