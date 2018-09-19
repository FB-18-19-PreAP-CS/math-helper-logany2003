from math import sqrt
'''
formula examples go here

'''


def quadratic(a,b,c):
    '''
returns the answer when entered a,b, and c from formula ax^2 + bx + c
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
        answer1 = (-b + sqrt(disc)) / (2*a)
        answer2 = (-b - sqrt(disc)) / (2*a)
        return answer1, answer2
    if disc == 0:
        answer = (-b) / (2*a)
        return answer
    
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
    answer = sqrt(pythag)
    return answer

def horizontal_asymptotes(a,b,c,d):
    '''
enter the powers for a and b and enter the coefficients for c and d. It gives you
the location of the horizontal asymptote
    >>> horizontal_asymptotes(3,2,2,3)
    'No horizontal asymptote'
    >>> horizontal_asymptotes(1,5,1,1)
    (0)
    >>> horizontal_asymptotes(1,1,2,1)
    (2.0)
    >>> horizontal_asymptotes(0,1,-1,1)
    (0)
    >>> horizontal_asymptotes(17,1,1,0)
    'No horizontal asymptote'
    '''
    if determine_powers(a,b) == "divide":
        return divide_coef(c,d)
    else:
        return determine_powers(a,b)
        
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
        return "No horizontal asymptote"

def divide_coef(a,b):
    '''
input the leading coefficients of the function to determine the location of the
horizontal asymptote
    '''
    location = a / b
    return location

def compound_interest(principal, rate, compound_amount, time):
    '''
takes in the initial amount, interest rate(as a decimal), amount of times interest is compounded
per year, and the time in years
    >>> compound_interest(0,0,0,0)
    '''
    if compound_amount == 0:
        return "you cannot compound interest 0 times a year"
    amount = principal*(1 + (rate/compound_amount))**(compound_amount*time)
    amount = round(amount,2)
    return amount
    
def distance(x1,y1,x2,y2):  
    dist = sqrt((x1-x2)**2 + (y1-y2)**2 )
    return dist
