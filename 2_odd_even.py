#https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# If the number is a multiple of 4, print out a different message.

# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

# user_number = int(input('tell me a number'))

# def is_odd_even(num):
#     if user_number % 4 == 0:
#         print(f'{user_number} can be divided by 4')
#     elif user_number % 2 == 0:
#         print(f'{user_number} is an even number')
#     else:
#         print(f'{user_number} is an odd number')

# is_odd_even(user_number)   
# 

num = int(input('give me a number'))
check = int(input('give me a number to divide that number by'))

if num % check == 0:
    print('your number divides evenly 🙌')
else:
    print('your number doesn\'t divide evenly 😥')