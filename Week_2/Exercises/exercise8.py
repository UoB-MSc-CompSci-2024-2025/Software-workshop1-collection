# Problem 8
# Given the following 2 functions, write the calling function.
# def the_function(num1, num2, num3):
# print(num1, num2, num3)
# def another(*args):
# the_function(*args)
#function call here

def first_function(num1, num2, num3):
    print(num1, num2, num3)

def second_function(*args):
    first_function(*args)

second_function(1, 2, 3)