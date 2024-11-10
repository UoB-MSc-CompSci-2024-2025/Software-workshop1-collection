# If-else selection
# 1. Write a program which asks the user for an integer
# number. The program should print “The war is over!!” if
# the number is exactly 1945, otherwise do nothing.

def war_track():
    year = int(input('Enter the year: '))
    if year == 1945:
        print('The war is over!!')
    else:
        return


# 2. Write a program which asks the user for an integer
# number. If the number is less than zero, the program
# should print out the number multiplied by -1. Otherwise,
# the program prints out the number as is. For example, if
# -9 is inputted then the output should be 9. If 150 is
# inputted, then the output should be 150.

def convert_negative_to_positive_number():
    num = int(input('Enter any negative or positive number: '))
    if num < 0:
        num = num * -1
        print(f'The converted negative value is {num}')
    else:
        print(f'The number is: {num}')


# 3. Write program that asks the user for 2 numbers and an
# operation. If the operation is add, multiply or subtract,
# the program should calculate and print out the result of
# the operation with the given numbers. If the user types
# anything else, the program should print out nothing. For
# example, if the numbers are 4 and 5 and the operation is
# add, then the output should be as follows:
# number 1: 4
# number 2: 5
# operation: add
# 4 + 5 = 9

def get_numbers():
    num1 = int(input('Enter number1: '))
    num2 = int(input('Enter number2: '))
    return num1, num2


def print_number(*args):
    print(f'number 1: {args[0]}')
    print(f'number 2: {args[1]}')

def get_operator(*args):
    operation = input('Enter for the operation needs to perform:')
    print(f'The Operation: {operation}')
    if operation == 'Add' or operation == 'add' or operation == '+' or operation == 'Addition':
        print_number(args[0], args[1])
        print(f'{args[0]} + {args[1]} = {args[0] + args[1]}')
    elif operation == 'Sub' or operation == 'sub' or operation == '-' or operation == 'Subtract':
        print_number(args[0], args[1])
        print(f'{args[0]} - {args[1]} = {args[0] - args[1]}')
    elif operation == 'Mul' or operation == 'mul' or operation == '*' or operation == 'x' or operation == 'Multiply':
        print_number(args[0], args[1])
        print(f'{args[0]} * {args[1]} = {args[0] * args[1]}')
    else:
        return

# def get_operator(num_one, num_two):
#     operation = input('Enter for the operation needs to perform:')
#     print(f'The Operation: {operation}')
#     if operation == 'Add' or operation == 'add' or operation == '+' or operation == 'Addition':
#         print_number(num_one, num_two)
#         print(f'{num_one} + {num_two} = {num_one + num_two}')
#     elif operation == 'Sub' or operation == 'sub' or operation == '-' or operation == 'Subtract':
#         print_number(num_one, num_two)
#         print(f'{num_one} - {num_two} = {num_one - num_two}')
#     elif operation == 'Mul' or operation == 'mul' or operation == '*' or operation == 'x' or operation == 'Multiply':
#         print_number(num_one, num_two)
#         print(f'{num_one} * {num_two} = {num_one * num_two}')
#     else:
#         return


# 4. Write a program which asks for the hourly wage, hours
# worked and the day of the week. The program should then
# print out the daily wages, which equal hourly wage
# multiplied by hours worked, except on Sundays when the
# hourly wage is double. The output could look as follows:
# hourly wage: 8.5
# hours worked: 3
# day of the week: Monday
# daily wages: 25.5 pounds
# hourly wage: 12.5
# hours worked: 10
# day of the week: Sunday
# daily wages: 250.0 pounds


def get_wage_and_hours_worked_details():
    hourly_wage = float(input('Enter the hourly wage: '))
    hours_worked = float(input('Enter hours worked: '))
    day_of_week = input('Enter the day of the week: ')
    return hourly_wage, hours_worked, day_of_week


def print_daily_wages(*args):
    print(f'hourly wage: {args[0]}')
    print(f'hours worked: {args[1]}')
    print(f'day of the week: {args[2]}')
    print(f'daily wages: {args[3]}')


def daily_wages(hourly_wage, hours_worked, day_of_week):
    if day_of_week == 'Sunday' or day_of_week == 'sunday':
        print_daily_wages(hourly_wage, hours_worked, day_of_week, (hourly_wage * 2) * hours_worked)
    else:
        print_daily_wages(hourly_wage, hours_worked, day_of_week, hourly_wage  * hours_worked)


# Write a program which asks for tomorrow’s weather
# forecast and then suggests weather-appropriate clothing.
# The suggestion should change if the temperature is over
# 20, 10 or 5 degrees and if there is rain on the way. The
# output could look as follows:
# what is the weather forecast for tomorrow?
# temperature: 21
# will it rain (yes / no): no
# wear jeans and a T
# what is the weather forecast for tomorrow?
# temperature: 10
# will it rain (yes / no): no
# wear jeans and a T
# a jumper is recommended
# what is the weather forecast for tomorrow?
# temperature: 3
# will it rain (yes / no): yes
# wear jeans and a T
# a jumper is recommended
# take a warm coat
# take an umbrella

def weather_checker():
    print('what is the weather forecast for tomorrow?')
    temperature = int(input('temperature: '))
    yes_or_no = input('will it rain (yes/no) ')
    return temperature, yes_or_no


def clothing_suggestion(temperature, yes_or_no):
    if temperature >= 20:
        if yes_or_no == 'yes':
             print('wear jeans and a T')
             print('take an umbrella')
        else:
            print('wear jeans and a T')
    elif 10 >= temperature < 20:
        if yes_or_no == 'yes':
          print('wear jeans and a T')
          print('a jumper is recommended')
          print('take an umbrella')
        else:
            print('wear jeans and a T')
            print('a jumper is recommended')

    elif temperature < 10:
        if yes_or_no == 'yes':
          print('wear jeans and a T')
          print('a jumper is recommended')
          print('take a warm coat')
          print('take an umbrella')
        else:
            print('wear jeans and a T')
            print('a jumper is recommended')
            print('take a warm coat')

# result1, result2 =  weather_checker()
# clothing_suggestion(result1, result2)