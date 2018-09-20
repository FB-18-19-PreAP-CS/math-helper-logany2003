from math import sqrt
'''
formula examples go here

'''


def quadratic(a,b,c):
    '''
returns the answer when entered a,b, and c from formula ax^2 + bx + c
    >>> quadratic(1,2,3)
    You can not have a negative or zero length
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
        raise ValueError("You can not divide by zero")
    if disc < 0:
        raise ValueError("No real solutions")
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
    13.0
    
    >>> pythagorean(24,7)
    25.0
    
    >>> pythagorean(4,3)
    5.0
    
    >>> pythagorean(9,12)
    15.0
    
    >>> pythagorean(-1, 10)
    Traceback (most recent call last):
        ...
    ValueError: You can not have a negative or zero length
    
    '''
    if a <= 0:
        raise ValueError("You can not have a negative or zero length")
    if b <= 0:
        raise ValueError("You can not have a negative or zero length")
    pythag = a**2 + b**2
    answer = sqrt(pythag)
    return answer

def horizontal_asymptotes(a,b,c,d):
    '''
enter the powers for a and b and enter the coefficients for c and d. It gives you
the location of the horizontal asymptote
    >>> horizontal_asymptotes(3,2,2,3)
    Traceback (most recent call last):
        ...
    ValueError: No horizontal asymptote
    
    >>> horizontal_asymptotes(1,5,1,1)
    0
    
    >>> horizontal_asymptotes(1,1,2,1)
    2.0
    
    >>> horizontal_asymptotes(0,1,-1,1)
    0
    
    >>> horizontal_asymptotes(17,1,1,0)
    Traceback (most recent call last):
        ...
    ValueError: No horizontal asymptote
    
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
        raise ValueError("No horizontal asymptote")

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
    Traceback (most recent call last):
        ...
    ValueError: you cannot compound interest 0 times a year
    
    >>> compound_interest(1200,.1249,12,.5)
    1276.92
    
    >>> compound_interest(10000,.08,4,1)
    10824.32
    
    >>> compound_interest(12500,.045,4,8)
    17880.64
    
    >>> compound_interest(4000,.08,4,1)
    4329.73
    '''
    if compound_amount == 0:
        raise ValueError("you cannot compound interest 0 times a year")
    amount = principal*(1 + (rate/compound_amount))**(compound_amount*time)
    amount = round(amount,2)
    return amount
    
def distance(x1,y1,x2,y2):
    '''
returns the distance between 2 points
    >>> distance(0,2,-1,-4)
    6.0828
    
    >>> distance(1,3,7,8)
    7.8102
    
    >>> distance(-2,3,3,-9)
    13.0
    
    >>> distance(1,-4,-4,2)
    7.8102
    
    >>> distance(-1,-15,0,0)
    15.0333
    '''
    dist = sqrt((x1-x2)**2 + (y1-y2)**2 )
    dist = round(dist, 4)
    return dist

def main():
    print("Welcome to the math helper.")
    print("There are five functions that you can use. They are quadratic,")
    print("pythagorean, horizontal_asymptotes, compound_interest, and distance.")
    print("For quadratic put in a 1, for pythagorean put in 2, for horizontal_asymptotes put in 3,")
    print("for compound_interest, put in 4, and for distance put in 5.")
    select = input("select which function to use")
    if select == "1":
        print("enter the a, b, and c in the function ax^2 + bx + c to get the value of the zeros")
        quadratic(a,b,c)
    elif select == "2":
        print("enter the a and b values on the equation a^2 + b^2 = c^2 to get the length of the hypotanuse of a right trianle")
        pythagorean(a,b)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #main()
    
    
    