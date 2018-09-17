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
    (-5.0, -5.0)
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
    
def pyhtagorean_theorm():
    pass
quadratic(5,6,1)