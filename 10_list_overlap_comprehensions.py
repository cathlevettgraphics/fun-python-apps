#   years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
#   ages = [2014 - year for year in years_of_birth]
# The second line here - the line with ages is a list comprehension.

# https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

# write a program that returns a list that contains only the elements that are common between the lists (without duplicates).

# x = [1, 2, 3]
# y = [5, 10, 15]
# allproducts = [a*b for a in x for b in y]
# print(allproducts)

# In general, the list comprehension takes the form:
# [EXPRESSION FOR_LOOPS CONDITIONALS]



list1 = [10, 20, 30, 40, 50]
list2 = [10, 10, 10, 20]

duplicates = [i for i in list1 if i in list2]
print(duplicates)


