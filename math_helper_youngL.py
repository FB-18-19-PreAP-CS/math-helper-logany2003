from math import sqrt
'''
formula examples go here

'''


def quadratic(a,b,c):
    '''
returns the awnser when entered a,b, and c from formula ax^2 + bx + c
    >>> quadratic(1,2,3)
    'No real solutions'
    >>> quadratic(5,3,3)
    'No real solutions'
    >>> quadratic(5,6,1)
    (-0.2, -1.0)
    >>> quadratic(3,10,-25)
    (1.67, -5.0)
    >>> quadratic(1,2,-3)
    (1.0, -3.0)
    '''
    disc = (b**2) - (4*a*c)
    if a==0:
        return "You have divided by zero, error"
    if disc < 0:
        return "No real solutions"
    if disc > 0:
        awnser1 = (-b + sqrt(disc)) / (2*a)
        awnser2 = (-b - sqrt(disc)) / (2*a)
        return awnser1, awnser2
    if disc == 0:
        awnser = (-b) / (2*a)
        return awnser
    
def pythagorean(a,b):
    '''
checks and uses the equation a^2 + b^2 = c^2 to determine the length of a
hypotanuse on a right triangle
    >>> pythagorean(5,12)
    (13.0)
    >>> pythagorean(24,7)
    (25.0)
    >>> pythagorean(4,3)
    (5.0)
    >>> pythagorean(9,12)
    (15.0)
    >>> pythagorean(-1, 10)
    'You can not have a negative or zero length'
    '''
    if a <= 0:
        return "You can not have a negative or zero length"
    if b <= 0:
        return "You can not have a negative or zero length"
    pythag = a**2 + b**2
    awnser = sqrt(pythag)
    return awnser

def horizontal_asymptotes(a,b):
    
    if determine powers(a,b) == "divide":
        divide_coef(c,d)
    
def determine_powers(a,b):
    '''
input the powers of the top and bottom of the fraction and determines where the
horizontal asymptote will be
    '''
    if a < b:
        return 0
    if a == b:
        return "divide"
    if a > b:
        return "None"

def divide_coef(a,b):
    '''
input the leading coefficients of the function to determine the location of the
horizontal asymptote
    '''
    location = a / b
    return location

def interest:
    pass