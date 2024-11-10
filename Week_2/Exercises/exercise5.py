# Problem 5
# Write a function that accepts one integer value. The function
# contains the following word = “thinking”. Return the word duplicated
# over and over, depending on argument passed in. for example if the
# number was 7, then the output should be
# thinkingthinkingthinkingthinkingthinkingthinkingthinking

def print_thinking(num):
    word = "thinking"
    for i in range(num):
        print(word, end="")

# print_thinking(7)

# Alternative
print('--- Alternative solution ---')

def repeater(times):
    repeated_value = 'thinking' * times
    print(f'you requested {times} time to repeat the {repeated_value}')

repeater(7)