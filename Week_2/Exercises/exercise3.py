# Problem 3
# Write a program which estimates a user's typical food expenditure.
# The program asks the user how many times a week they eat out. Then it
# asks for the price of a typical student lunch, and for money spent on
# groceries during the week. Based on this information the program
# calculates the user's typical food expenditure both weekly and daily.
# The program should function as follows:
# How many times a week do you eat out? 4
# what is the price of a typical student lunch? 4.95
# How much money do you spend on groceries in a week? 45.50
# Average food expenditure: Daily: 9.33 Weekly: 65.3

eating_out = int(input("How many times do you eat out per week? "))
price_of_lunch = float(input("What is the average cost of a student lunch? "))
price_of_groceries = float(input("What is the average cost of doing your groceries? "))

weekly_expenditure = round(eating_out * price_of_lunch + price_of_groceries)
daily_expenditure = round(weekly_expenditure / 7)

print(f"Average food expenditure: Daily: {daily_expenditure}. Weekly: {weekly_expenditure}")