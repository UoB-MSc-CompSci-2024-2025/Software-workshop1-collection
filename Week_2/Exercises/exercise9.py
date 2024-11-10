# Given the following function, create a function call to display a
# name, age and location and another one that just shows the name and
# age.
# def create_profile(**kwargs):
# profile = {
# 'name': kwargs.get('name', 'Unknown'),
# 'age': kwargs.get('age', 'Unknown'),
# 'location': kwargs.get('location', 'Unknown')
# }
# return profile
# #function calls here


def create_profile(**kwargs):
    profile = {"name": kwargs.get("name", "Unknown"), "age": kwargs.get("age", "Unknown"), "location": kwargs.get("location", "Unknown")}
    for x, y in profile.items():
        print(f"{x}: {y}")
    return profile

create_profile(name="Kesh", age="24", location="Birmingham")

create_profile(name="Kesh", age="24")

# Alternative
print('--- Alternative solution ---')

def create_profile_alternative(**kwargs):
    profile = {
    'name': kwargs.get('name', 'Unknown'),
    'age': kwargs.get('age', 'Unknown'),
    'location': kwargs.get('location', 'Unknown')
    }
    return profile

def display_profile(**kwargs):
    print(f"Your name is {kwargs['profile']['name']}")
    print(f"Your age is {kwargs['profile']['age']}")

display_profile(profile = create_profile_alternative(name= 'Logesh', age= 28, location= 'LocationXXx'))
