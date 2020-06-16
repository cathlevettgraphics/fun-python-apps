# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).

def get_int():
    return int(input('give me a number')) 

number = get_int()
answers = []

for i in range(1, number + 1):
    if number % i == 0 and i != 1 and i != number:
        answers.append(i)

if len(answers) == 0:
    print(f'{number} is a prime number')
else:
    print(f'{number} is not a prime number')      

# print(answers)
          


          