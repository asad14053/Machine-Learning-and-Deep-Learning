# Complete the following math utility functions

'''
Python Raw Coding by a C/C++ expert
Compiled by:
Md. Asaduzzaman Jabin
Ph.D. Student, ECE, UGA
'''

import math
from math import dist, sqrt
# You may need to add an import

def pythagorean_theorem(a,b):
    # Input: a,b as the two perpendicular sides of a right triangle
    # Output: the length of the hypotenuse
    return sqrt(a**2+b**2) #solved for you.  Solve the 5 problems below.

def calculate_triangle_area(a,b,c):
    # Input: a,b,c as the lengths of the 3-side of a triangle
    # Output: triangle area

    a = float(a)
    b = float(b)
    c = float(c)
    s = float(a+b+c)/2.0  #  Perimeter
    area = sqrt(s*(s-a)*(s-b)*(s-c))  # Heron's formula for area of triangle
    return area

def calculate_triangle_angles(a,b,c):
    # Input: a,b,c as the lengths of the 3-side of a triangle
    # Output: 3-tuple (alpha,beta,gamma) as the 3 angles opposing (a,b,c) respectively)

    a = float(a)
    b = float(b)
    c = float(c)
    A = math.acos((b**2+c**2-a**2)/(2*b*c))   # formula: a**2 = b**2 + c**2 - 2*b*c*Cos A
    B = math.asin(b*math.sin(A)/a)  #formula : Sin A/ a = Sin B/ b 
    C = math.asin(b*math.sin(A)/a)  #formula : Sin A/ a = Sin C/ c
    return A,B,C  #return radian

def solve_quadratic(a,b,c):
    # Input: a,b,c as the coefficients a genderal quadratic equation a*x^2 + b*x + c = 0
    # Output: a 2-tuple as the solutions to x

    a = float(a)
    b = float(b)
    c = float(c)
    x1 = (-b+sqrt(b**2-4*a*c))/(2.0*a)  #solution of a quadratic equation, x = (-b +- sqrt(b**2-4ac))/(2a) 
    x2 = (-b-sqrt(b**2-4*a*c))/(2.0*a)
    return x1, x2

def newton_gravity(m1_kg,m2_kg,dist_m):
    # Input: masses of the two objects in kilograms, and the distance in meters between them
    # Output: the gravitational force between the object (in Newtons) according to Newton's universal law of gravitation
    # Note: G = 6.674e-11 m^3/(kg*s^2) should be used

    # if all units are in correct form, then
    m1_kg = float(m1_kg)
    m2_kg = float(m2_kg)
    dist_m = float(dist_m)
    G = 6.674e-11
    F = G*m1_kg*m2_kg/ (dist_m**2)  # force F(newton) = G* (m1*m2)/R^2
    return F  #unit newton

def normal_distribution(x,mu,sigma):
    # Input: x is the input to the normal distribution, mu and sigma are the mean and standard deviation
    # Output: returns the value of the normal probability distribution function at x
    
    x = float(x)
    mu = float(mu)
    sigma = float(sigma)

    #formula norm = (math.exp(-(float(x)-float(mean))^2/(2*var)))/((2*math.pi*var)^.5)
    
    varience = sigma**2
    denom = (2*math.pi*varience)**0.5
    norm = math.exp(-(x-mu)**2/(2*varience))/denom
    return norm

# x = calculate_triangle_area(3,4, 5)
# print(x)
# x, y, z = calculate_triangle_angles(3,4, 5)
# print(x,y,z)
# x, y = solve_quadratic(1,1, -12)
# print(x,y)
# x = newton_gravity(7,5,5)
# print(x)
# x = normal_distribution(7,5,5)
# print(x)

'''
Output:
r/Info 8000/assignment-3-functions-and-class.............../math_utilities.py"
6.0
0.6435011087932843 0.927295218001612 0.927295218001612
3.0 -4.0
9.3436e-11
0.07365402806066466
'''