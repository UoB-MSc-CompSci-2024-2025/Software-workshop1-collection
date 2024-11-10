# Problem 10
# Given the function call, write the function to find the minimum
# and maximum numbers, make use of min() and max() functions to
# accomplish this.
# function call:
# the_min, the_max = find_min_max(2, 5, 7, 9, 10, 1)
# print(the_min, the_max)

def find_min_max(*args):
    maximum = max(args)
    minimum = min(args)
    return minimum, maximum

the_min, the_max = find_min_max(1, 5, 24, 7, 87, 23, 45, 9)
print(f'the_min {the_min}, the_max {the_max}')

# Alternative
print('--- Alternative solution ---')
# we can avoid to introduce new variable

def find_min_max_alternative(*args):
  return  min(args), max(args)

the_min, the_max = find_min_max(1, 5, 24, 7, 87, 23, 45, 9)
print(f'the_min {the_min}, the_max {the_max}')