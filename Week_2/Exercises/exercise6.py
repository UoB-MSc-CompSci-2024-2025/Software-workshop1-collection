# Problem 6

# Create a function like this:|
# def summing(*args):
# return sum(args)
# Call the function 3 times, the first time passing 3 nums, the 2nd
# time passing 6 numbers and the 3rd time passing 10 nums.

def summing(*args):
    return sum(args)

# by this way we can reduce the computation by calling the sum only one time.

print(f'first time passing 3 nums: {summing(1, 2, 4)}')
print(f'first time passing 6 nums: {summing(1, 2, 3, 4, 5, 6)}')
print(f'first time passing 10 nums: {summing(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')