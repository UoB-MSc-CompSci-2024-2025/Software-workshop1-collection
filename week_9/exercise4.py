# Q4. Create two classes that inherit from the Pizza class (See the code below)
# • PizzaMargherita class. Instance a:ribute: has_extra_cheese
# • PizzaMarinara class. Instance a:ribute: has_extra_basil
# • These two classes must inherit all the instance a:ributes of the Pizza class.
# • Create two instances, one of each subclass and assign them to their corresponding
# variable
# class Pizza:
# def __init__(self, size, toppings, price, rating):
# self.size = size # "Small", "Medium", or "Large"
# self.toppings = toppings # A list of toppings
# self.price = price
# self.rating = rating # Scale from 1 to 5
# # Add the subclasses below this line

class Pizza:
    def __init__(self, size, toppings, price, rating):
        self.size = size  # "Small", "Medium", or "Large"
        self.toppings = toppings  # A list of toppings
        self.price = price
        self.rating = rating  # Scale from 1 to 5


class PizzaMargherita(Pizza):
    def __init__(self, size, toppings, price, rating, has_extra_cheese):
        self.has_extra_cheese = has_extra_cheese
        super().__init__(size, toppings, price, rating)


class PizzaMarinara(Pizza):
    def __init__(self, size, toppings, price, rating, has_extra_basil):
        self.has_extra_basil = has_extra_basil
        super().__init__(size, toppings, price, rating)
