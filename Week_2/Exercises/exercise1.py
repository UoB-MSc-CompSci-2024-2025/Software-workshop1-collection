# Problem 1
# Write the code that will ask the user for their height and weight.
# The program must calculate their BMI using the formula weight /
# (height * height). Print out their weight, height and BMI, each on
# separate lines and include a description of each, like this:
# Your weight is: 60kg
# Your height is: 1.7m
# your BMI is: 21

height = float(input("How tall are you? "))
weight = int(input("How much do you weigh? "))
BMI = round(weight / (height * height))

print(f"Your height is {height}m")
print(f"Your weight is {weight}kg")
print(f"Your BMI is {BMI}")

