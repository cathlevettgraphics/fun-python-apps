# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_list = []

for num in a:
    if num % 2 == 0:
        new_list.append(num)
print(new_list)      


comp_list_new = [(num) for num in a if num % 2 == 0 ]
print(comp_list_new)


# example
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991, 1980]
ages = [2020 - year for year in years_of_birth]
print(ages)  


# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
# >>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]