# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

# keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.


from random import randint

random_number = randint(1, 10)
print(random_number)
count = 0

while True:
        user_guess = input('guess a number between one and nine: ')
        if user_guess == 'exit':
                break
       
        user_guess = int(user_guess)
        count += 1

        if user_guess == random_number:
                print(f'you guessed just right! It took {count} attempts')
                break

        if user_guess > 10 or user_guess < 0:
                print('out of range, try again')
        elif user_guess > random_number:
                print('you guessed to high')
        else: print('you guessed to low')   