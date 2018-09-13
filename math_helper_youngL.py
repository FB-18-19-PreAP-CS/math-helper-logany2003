from math import *
'''
formula examples go here

'''


def quadratic_formula(a,b,c):
    '''
returns the awnser when entered a,b, and c from formula ax^2 + bx + c
    '''
    if a==0:
        return "You have divided by zero, error"
    x = (b**2) - (4*a*c)
    y = math.sqrt(x)
    print(y)

def pyhtagorean_theorm():
    pass