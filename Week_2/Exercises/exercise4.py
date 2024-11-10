# Problem 4
# Make use of functions.py (provided to you from Canvas). Create a new
# function called average(). Pass 3 marks to the function, calculate
# the average and print the average in the function. Remember to call
# the function appropriately.

def average(num1, num2, num3):
    mean = (num1 + num2 + num3) / 3
    # changed variable name from average to mean -> already we have defined function as average
    # it's always good practice to have different name for local variables
    print(mean)
    return mean

average(num1=3, num2=5, num3=9)