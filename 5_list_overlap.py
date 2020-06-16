# Take two lists, say for example these two:


# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# https://www.techbeamers.com/python-generate-random-numbers-list/
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random

list_random_1 = [random.randint(1, 20) for iterable in range(20)]
list_random_2 = [random.randint(1, 20) for iterable in range(15)]
print(list_random_1)
print(list_random_2)

# a = [1, 1, 1, 2, 3, 5, 8, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
in_both_lists = []

for num in list_random_1:
    if num in list_random_2 and num not in in_both_lists:
        in_both_lists.append(num)
print(in_both_lists)        