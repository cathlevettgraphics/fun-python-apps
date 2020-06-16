# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.

# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html



def fibonacci(how_many):
    a = 0
    b = 1
    count = 0
    while count < how_many:
        print(a)
        next_num = a + b
        a = b
        b = next_num
        count += 1

fibonacci(28)