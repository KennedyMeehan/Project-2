import math

def circle(first_num):
    
    '''Calculates the area of a circle given an user input

        if user gives invalid input, displays a message to guide user.
    '''
    
    first_num = float(first_num)
    if first_num <= 0:
        raise TypeError("Values must be positive")
    return math.pi * (first_num ** 2)


def square(first_num):
    '''Calculates the area of a square given an user input

        if user gives invalid input, displays a message to guide user.
    '''
    first_num = float(first_num)
    if first_num <= 0:
        raise TypeError("Values must be positive")
    return first_num ** 2


def rectangle(first_num, second_num):
    '''Calculates the area of a rectangle given an two user inputs.

        if user gives invalid input, displays a message to guide user.
    '''
    first_num = float(first_num)
    second_num = float(second_num)
    if first_num <= 0 or second_num <= 0:
        raise TypeError("Values must be positive")
    return first_num * second_num

def triangle(first_num, second_num):
    '''Calculates the area of a Triangle given two user inputs

        if user gives invalid input, displays a message to guide user.
    '''
    first_num = float(first_num)
    second_num = float(second_num)
    if first_num <= 0 or second_num <= 0:
        raise TypeError("Values must be positive")
    return 0.5 * first_num * second_num
