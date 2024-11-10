# # Problem 2
# If we want to total some numbers up we can do it as follows:
# sum = 0
# number = int(input(“enter the first number”))
# sum += number ====> sum = sum + number
# number = int(input(“enter the second number”))
# sum += number
# number = int(input(“enter the third number”))
# sum += number
# print(“The sum of the numbers is”, sum)
# How can we achieve this without using the variable number (we would
# still have 3 input lines)

sum = 0
sum += int(input("enter the frst number: "))
sum += int(input("enter the second number: "))
sum += int(input("enter the third number: "))

print(f"The sum of the numbers is {sum}")

