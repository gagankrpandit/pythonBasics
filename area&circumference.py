# Python program to find the circumference and area of a circle with a given radius
from cmath import pi


radius = int(input('Enter the radius of circle in cms: '))

def circumference(radius):
    c = 2 * pi * radius
    print(f'The circumference for radius {radius} is {c} cm')

def area(radius):
    a = pi * (radius**2)
    cm = str.maketrans("2", "²")
    print(f'The area for radius {radius} is {a}', "cm2".translate(cm))

circumference(radius)
area(radius)

# print("⁰¹²³⁴⁵⁶⁷⁸⁹")
