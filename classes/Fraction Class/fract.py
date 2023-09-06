# Author: DerVogel101
# Description: A simple fraction class with some basic functions
# Date: 04.09.2023
# Task:
# Convert the functions from a previous task(functions.py) to a class.

from typing import Self

class Fract:
    def __init__(self, nominator, denominator):
        self.fract = [nominator, denominator]
        self.nominator = nominator
        self.denominator = denominator
        self.highest_divisor = self.denominator

    def cancel(self):
        nominator = self.nominator
        denominator = self.denominator
        highest_divisor = denominator
        for divisor in range(1, denominator + 1):
            if nominator % divisor == 0 and denominator % divisor == 0:
                highest_divisor = divisor
        return Fract(nominator // highest_divisor, denominator // nominator)

    def ggt(self):
        a = self.nominator
        b = self.denominator
        while b != 0:
            h = a % b
            a, b = b, h
        return a

    def neg(self):
        return Fract(-1 * self.nominator, self.denominator)

    def __str__(self):
        return f"{self.nominator}/{self.denominator}"

    def __add__(self, other):
        a, b = self.nominator, self.denominator
        c, d = other[0], other[1]
        return Fract(a * d + c * b, b * d)

    def __sub__(self, other):
        a, b = self.nominator, self.denominator
        c, d = other[0], other[1]
        return Fract(a * d - c * b, b * d)

    def __mul__(self, other):
        a, b = self.nominator, self.denominator
        c, d = other[0], other[1]
        return Fract(a * c, b * d)

    def __truediv__(self, other):
        a, b = self.nominator, self.denominator
        c, d = other[0], other[1]
        return Fract(a * d, b * c)

    def __iter__(self):
        return iter(self.fract)

    def __getitem__(self, index) -> int:
        return self.fract[index]

    def __float__(self) -> float:
        """Returns the decimal value of the fraction."""
        return self.nominator / self.denominator

    def __int__(self) -> int:
        """Returns the integer part of the fraction, this cuts off the decimal part."""
        return self.nominator // self.denominator

    def __eq__(self, other) -> bool:
        return self.nominator == other[0] and self.denominator == other[1]

    def __dict__(self) -> dict[str, int]:
        return {"nominator": self.nominator, "denominator": self.denominator, "decimal": float(self)}

    def __repr__(self) -> str:
        return f"Fract({self.nominator}, {self.denominator})"

    #@classmethod
    #def from_decimal(cls, decimal: float) -> Self:

