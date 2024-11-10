# Problem 7
# Write a function using *args and **kwargs that prints out the
# arguments passed to it, using the following function calls:
# the_function(5, 10, stud_nbr="12345", mod_code="SWW1")
# the_function(8, 7, stud_nbr="56784", mod_code="SWW1")
# Do you know which arguments are positional and which are keyword? yes

def exercise(*args, **kwargs):
    for argument in args:
        print(argument)
    for key, value in kwargs.items():
        print(f"key = {key}, value = {value}")

exercise(5, 10, stud_nbr="12345", mod_code="SWW1")

# *args -> works like a list [5, 10]
# **kwargs -> works like a dictionary {key : value} -> {"stud_nbr" : "12345", "mod_code" : "SWW1" }