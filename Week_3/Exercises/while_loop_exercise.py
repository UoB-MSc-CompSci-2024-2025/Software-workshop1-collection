# 2. This program has some syntactic issues, fix them so that
# the output is correct:
# print(“Let’s do this”)
# num = int(input(“Enter a number:”)
# while num =0:
# print(num)
# print(“DONE!!!”)
# Output:
# Enter a number:5
# 5
# 4
# 3
# 2
# 1
# DONE!!!

num = int(input("Enter a number: "))

while num > 0:
    print(num)
    num -= 1


print('DONE!!!')


# In the game of Lucky Sevens, the player rolls a pair of
# dice. If the dots add up to 7, the player wins £4,
# otherwise the player loses £1. You need to write a
# program that should take as input the amount of money
# that the player wants to put into the pot and play the
# game until the pot is empty. At that point, the program
# should print the number of rolls it took to break the
# player, as well as the maximum amount of money in the
# pot.


# Make use of a nested while loop to achieve the following
# output of building a pyramid of numbers:
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1
# 0

def revers_pyramid():
    column = 0
    row = 0
    compare_value = 5
    while column <= 5:
        while row < compare_value:
            print(f'{row} ', end='')
            row += 1
        print('\n')
        compare_value -= 1
        row = 0
        column += 1




revers_pyramid()