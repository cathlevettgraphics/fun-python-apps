# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

# https://note.nkmk.me/en/python-random-choice-sample-choices/

import random

password_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '!', '@', '£', '$', '%', '&', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

weak = ['password', '123456', 'helloworld']


user_input = input('How strong would you like your password to be? weak or strong: ')

while user_input != 'quit':
    if user_input == 'weak':
        print(random.sample(weak, 1))
        break
    elif user_input == 'strong':
        user_input = int(input('How many characters?: '))
        new_password = []
        new_password.append(random.sample(password_options, user_input))
        print(new_password)
        break
    else:
        user_input = input('please enter weak or strong, or enter quit to leave: ')



# def password_gen(length):
#     new_password = []
#     new_password.append(random.sample(password_options, length))
#     return (new_password)

# result = password_gen(8)        
# print(result)


        

        
        