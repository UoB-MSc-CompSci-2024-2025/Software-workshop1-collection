# Q2. Mammal and Panda: A>ribute Inheritance
# • Create a Panda class that inherits from the Mammal class (see below).
# • Make Panda inherit all the a:ributes defined in Mammal
# • Add a class a:ribute to Panda: is_endangered = True
# • Add an instance a:ribute: code
# • Create an instance of Panda and store it in the variable my_panda. You can choose
# any values as the arguments used to create the instance.
# class Mammal:
# def __init__(self, name, age, health, num_offspring,
# years_in_captivity):
# self.name = name
# self.age = age
# self.health = health
# self.num_offspring = num_offspring
# self.years_in_captivity = years_in_captivity
# # Define the Panda class below this line

class Mammal:
    def __init__(self, name, age, health, num_offspring,
                 years_in_captivity):
        self.name = name
        self.age = age
        self.health = health
        self.num_offspring = num_offspring
        self.years_in_captivity = years_in_captivity

class Panda(Mammal):
    is_endangered = True
    def __init__(self, name, age, health, num_offspring,years_in_captivity, code):
        super().__init__(name,age,health,num_offspring,years_in_captivity)
        self.code = code

my_panda = Panda('Hardik', '5', True, '4', '6', 'HP')
