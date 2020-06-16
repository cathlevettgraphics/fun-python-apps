#https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

name = input('what is your name?')
age = int(input('what is your age?'))
year = 2020
num_copies = int(input('print this many copies of the message'))

print(f'{name}, you will turn 100 in {year + (100 - age)} \n' * num_copies) 
