# 2. Create another function called all_modules().
# Include sww1 – as above and 2 others (any so that you have 3
# dictionaries each with a module name and the corresponding
# information).
# Create a list that holds the dictionary names just created
# above.
# Again, using a for loop print the contents in the following
# way:
# Information regarding all modules:
# How is the module assessed? t
# Which term is the module taught? 1
# How much weighting is given to the assessments? 100
# How is the module assessed? e
# Which term is the module taught? 2
# How much weighting is given to the assessments? 80
# How is the module assessed? e
# Which term is the module taught? 1
# How much weighting is given to the assessments? 100

def all_modules():
    sww1 = {'type_assess': 't', 'term': 1, 'weighting': 100}
    dsa = {'type_assess': 'e', 'term': 2, 'weighting': 80}
    ai_ml = {'type_assess': 'e', 'term': 1, 'weighting': 100}
    list_of_modules = [sww1, dsa, ai_ml]

    print("Information regarding all modules:")

    for module in list_of_modules:
        print(f"How is the module assessed? {module['type_assess']}")
        print(f"Which term is the module taught? {module['term']}")
        print(f"How much weighting is given to the assessments? {module['weighting']}")


# all_modules()


# 3. Lastly, create a nested dictionary using the dictionaries
# above where the dictionary is called msc_modules {} and each
# key is “sww1” (module name) followed by the rest of the
# dictionary as above. For example:
# msc_modules = {
# “sww1” : {‘type_assess’:’t’, ‘term’: 1, ‘weighting’: 100}
# #include the others here
# }
# Create a for loop to output the data in the following way:
# For sww1 the type of assessment is t The module is taught in term 1
# The weighting is 100
# For dsa the type of assessment is e The module is taught in term 2
# The weighting is 80
# For prof_prac the type of assessment is e The module is taught in
# term 1 The weighting is 100

def all_modules_for_nested():
    sww1 = {'type_assess': 't', 'term': 1, 'weighting': 100}
    dsa = {'type_assess': 'e', 'term': 2, 'weighting': 80}
    ai_ml = {'type_assess': 'e', 'term': 1, 'weighting': 100}
    msc_modules = {"sww1": sww1, "dsa": dsa, "ai_ml": ai_ml}

    print("Information regarding all modules:")

    for key, module in msc_modules.items():
        print(
            f"For {key} the type of assessment is {module['type_assess']} The module is taught in term {module['term']} The weighting is {module['weighting']}")

# all_modules_for_nested()

# 4.  Create a contacts dictionary. Write a function that adds a new
# contact, updates an existing one and retrieves a contact by
# name. include a series of prompts and a menu to facilitate
# this. For example. Your contacts could include:
# “Jack Smith”: {“phone”: “12345123”, “email”: “jsm @ gmail.com”},
# “Mary Hawkes”: {“phone”: “58678”, “email”: “jha @ gmail.com”},
# Add a contact:
# call the function and prompt for a name, phone number and
# email address; update the contacts {} – this is set as a
# global variable.
# Find a contact: a prompt should ask which contact to find
# using the full name, the function should print out the
# corresponding phone number and email if the contact is found
# Update a contact:
# a prompt should ask for a contacts full name to update; if the
# contact is found another prompt should ask about what to
# update 1 – phone number or 2 – mail; create the code to
# perform the update (use a loop that iterates over each
# dictionary item, finds the contact and makes the appropriate
# update) -> Important to test this functionality very well.
# list all contact:
# List all of the contacts in the dictionary using an
# appropriate format / styling.
# Using ChatGPT for learning

_contacts = {
    "Jack Smith": {"phone": "12345123", "email": "jsm@gmail.com"},
    "Mary Hawkes": {"phone": "58678", "email": "jha@gmail.com"},
}


def add_contact():
    name = input("Enter your full name: ")
    phone_number = input("Enter phone number: ")
    email_address = input("Enter email address: ")
    _contacts[name] = {"phone": phone_number, "email": email_address}


def find_contact():
    which_contact = input("Search with full name: ")

    if which_contact in _contacts:
        print(f"{_contacts[which_contact]} \n")
    else:
        print("Contact not found \n")

def update_contact():
    which_contact = input("Search with full name: ")

    if which_contact in _contacts:
        choice = int(input("Press: 1. Update phone number \n"
                              "Press: 2. Update email \n"
                              "Please make your choice: "))
        if choice == 1:
            update_phone(which_contact)
        elif choice == 2:
            update_email(which_contact)
        else:
            print("Please make a correct choice")
    else:
        print("Contact not found \n")



def update_phone(which_contact):
    phone_number = input("Enter phone number: ")
    _contacts[which_contact]['phone'] = phone_number


def update_email(which_contact):
    email_address = input("Enter email address: ")
    _contacts[which_contact]['email'] = email_address

def list_all_contact():
    for key, value in _contacts.items():
        print(f"Name: {key}, Phone: {value['phone']}, Email: {value['email']} \n")


def main():
    while True:
        choice = int(input(" Contact app \n"
                           "1. Add contacts \n"
                           "2. Find contact\n"
                           "3. Update contact\n"
                           "4. List all contacts\n"
                           "5. Exit\n"
                           "Please make your choice: "))

        match choice:
            case 1:
                add_contact()
                print(_contacts)
            case 2:
                find_contact()
            case 3:
                update_contact()
                print(_contacts)
            case 4:
                list_all_contact()
            case 5:
                add_contact()
            case _:
                print(" *** Please select from above option! *** \n")


if __name__ == '__main__':
    main()
