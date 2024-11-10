# Create a function called create_dict().
# Create a dictionary to store information about software
# workshop I. The dictionary should store the following
# information:
# type_assess – t is tests and e is exams, term and weighting.
# For example, a dictionary could look as follows:
# sww1 = {‘type_assess’:’t’, ‘term’: 1, ‘weighting’: 100}
# print a heading “Information regarding SWW1”
# Using a for loop print each key-pair like this:
# Information regarding software workshop I
# ('type_assess', 't')
# ('term', 1)
# ('weighting', 100)

def create_dict():
    sww1 = {'type_assess' : 't', 'term' : 1, 'weighting':100}
    print("Information regarding SWW1")
    for key,value in sww1.items():
        print((key,value))


create_dict()