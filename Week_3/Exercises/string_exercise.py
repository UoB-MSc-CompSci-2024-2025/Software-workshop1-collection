# Given a list of integers, we can decide that 2 items are
# neighbours if they differ by 1. For example, the list 2,
# 3, 5, 7, 9 would show that 2 and 3 are neighbours as they
# only differ by 1. If the list was 2, 3, 4, 5, 9 then 2
# and 3, 3 and 4, 4 and 5 are neighbours.
# a. Just think about / scribble down / code the
# following - Write a function that looks for the
# longest series of neighbours within the list and
# returns its length. For example, the above-mentioned
# list the longest list would be 2, 3, 4, 5 and the
# length would be 3.
# b. Now, use ChatGPT and ask for a solution (copy and
# paste the above problem to the prompt).
# c. Once you have completed reading ChatGPT’s code
# solution / explanation, please complete the survey
# using this QR code:

def longest_neighbour_series(nums):
    if not nums:  # Handle the case for an empty list
        return 0

    # Sort the list to arrange neighbours next to each other
    nums = sorted(nums)

    longest = 1  # To store the maximum length of consecutive neighbours
    current_streak = 1  # To track the current sequence of neighbours

    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] == 1:  # Check if current and previous numbers are neighbours
            current_streak += 1
        else:
            # If not neighbours, reset the current streak counter
            longest = max(longest, current_streak)
            current_streak = 1

    # In case the longest series is at the end
    longest = max(longest, current_streak)

    return longest


# # Example usage:
# nums = [2, 3, 4, 5, 6,7,8,9,10,11,12]
# print(longest_neighbour_series(nums))  # Output should be 4


def check_anagrams(word_one, word_two):
    checked_value = []
    word_one =  word_one.replace(' ', '_')
    word_two =  word_two.replace(' ', '_')
    print(f'{word_one} {word_two}')
    for letter_one in word_one:
        if letter_one == '_':
            continue
        else:
            for letter_two in word_two:
                if letter_one == '_':
                    continue
                elif letter_one == letter_two:
                        checked_value.append(True)

    if len(checked_value) == len(word_one) == len(word_two):
        print('yes it is anagrams')
    else:
        print('no it is not anagrams')

def check_anagrams_alternative(word_one, word_two):
    word_one = word_one.replace(' ', '').replace("'", '').lower()
    word_two = word_two.replace(' ', '').replace("'", '').lower()
    print(f'{word_one}, {word_two}')
    print(f'{len(word_one)}, {len(word_two)}')
    result = []
    for letter_one in word_one:
        for index, letter_two in enumerate(word_two):
            print(f'{letter_one} - {letter_two}')
            if letter_one == letter_two:
                word_two = word_two.replace(word_two[index], '-', 1)
                print(f'{word_two}')
                result.append(True)

    if len(word_one) == len(result):
        print('yes it is anagrams')
    else:
        print('no it is not anagrams')


def check_anagrams_two(word_one, word_two):
    word_one = word_one.replace(' ', '').replace("'", '').lower()
    word_two = word_two.replace(' ', '').replace("'", '').lower()
    word_one_list = []
    word_two_list = []
    for index in range(0, len(word_one)):
        word_one_list.append(word_one[index])

    for index in range(0, len(word_two)):
        word_two_list.append(word_two[index])

    word_one_list.sort()
    word_two_list.sort()
    print(f'{word_one_list} {word_two_list}')

    if word_one_list == word_two_list:
        print('yes it is anagrams')
    else:
        print('no it is not anagrams')


# check_anagrams('I\'m a dot in place', 'a decimal point')

# check_anagrams_alternative('eleven plus two', 'twelve plus one')

# getWordList('a decimal point', 'I\'m a dot in place')


_matrix = [[1, 2, 4],
           [3, 4,45]]


def sum_rows(matrix):
    sum_result = 0
    for element in matrix:
        for item in element:
            sum_result = sum_result + item

    print(f'{sum_result}')


def sum_columns(matrix):
    column1 = get_column(matrix, 0)
    column2 = get_column(matrix, 1)
    column3 = get_column(matrix, 2)
    matrix = [column1, column2, column3]
    sum_rows(matrix)


def get_column(matrix, column):
    print(f'column conversion {[val[column] for val in matrix]}')
    return [val[column] for val in matrix]


# sum_rows(_matrix)

sum_columns(_matrix)