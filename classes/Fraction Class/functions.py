# Author: DerVogel101 and Katzenkralle
# Description: Functions for Math operations with fractions
# Date: 21.08.2023
# Task:
# Create following functions:
# - printFract - prints a fraction
# - cancelFract - cancels a fraction
# - inputFrac - inputs a fraction
# - addFrac - adds two fractions
# - subFrac - subtracts two fractions
# - mulFrac - multiplies two fractions
# - divFrac - divides two fractions
# - ggtFrac - calculates the ggt of a fraction
# - negFrac - negates a fraction


def printFract(fract: tuple[int, int]) -> None:
    print(f"{fract[0]}/{fract[1]}")


def cancelFract(fract: tuple[int, int]) -> tuple[int, int]:
    nominator = fract[0]
    denominator = fract[1]
    highest_divisor = denominator
    for divisor in range(1, denominator + 1):
        if nominator % divisor == 0 and denominator % divisor == 0:
            highest_divisor = divisor
    return nominator // highest_divisor, denominator // nominator


def inputFrac():
    print("a / b = c")
    frac_num = [None, None]
    frac_var= ("a", "b")
    t = 0
    while frac_num[0] == None or frac_num[1] == None:
        try:
            frac_num[t] = input(f"{frac_var[t]} = ")
            frac_num[t] = int(frac_num[t])
            t += 1
        except TypeError:
            print("Input a Number!")
    return frac_num


def getGGT(a,b):
    while b != 0:
        h = a % b
        a,b = b,h
    return a


def negFrac(a, b):
    return [-1*a, b]


def multFrac(a,b, ba, bb):
    return [a*ba, b*bb]


def divFrac(a,b, ba, bb):
    return [a/ba, b/bb]


def addFrac(a,b, ba, bb):
    return [a*bb + ba*b, b + bb]

def subFrac(a,b, ba, bb):
    return [a*bb - ba*b, b + bb]
