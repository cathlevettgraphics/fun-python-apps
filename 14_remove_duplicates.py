# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Features of sets
# Sets are not ordered. This means that there is no “first element” or “last element.” There are just “elements”. You cannot ask a set for it’s “next element”.
# There are no repeat elements in sets.
# You can convert between sets and lists very easily.

# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
list = ['cath', 'andrew', 'vicky', 'ed', 'josy', 'cath', 'josy', 'cath']

no_duplicates = []
only_duplicates_list = []


# all elements of list minus duplicates
def remove_duplicates(el):
    for item in list:
        if list.count(item) == 1:
            no_duplicates.append(item)
    print(no_duplicates)

remove_duplicates(list)

#------------------------------------------------------

# all elements of list minus duplicates – using sets!!
def duplicates_single(el):
    el = set(el)
    print(el)

duplicates_single(list)

#------------------------------------------------------

# print only duplicates and print them only onnce
def only_duplicates(el):
    for item in list:
        if list.count(item) > 1 and item not in only_duplicates_list:
            only_duplicates_list.append(item)
    print(only_duplicates_list)  

only_duplicates(list)
