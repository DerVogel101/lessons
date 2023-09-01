# Author: DerVogel101
# Description: A simple circle class with some basic functions
# Date: 01.09.2023
# Task:
# Legen sie eine Klasse Circle.
# - Der Konstruktor soll einen Mittelpunkt und einen Radius übergeben bekommen.
# - Eine Methode soll den Umfang des Kreises zurückgeben.
# - Eine Methode soll die Fläche des Kreises zurückgeben.
# - Eine Methode soll den Radius um einen Faktor vergrößern.
# - Zusatz: Es soll die tnfernung zwischen zwei Kreisen ihren äußeren rändern berechnet werden können.


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
