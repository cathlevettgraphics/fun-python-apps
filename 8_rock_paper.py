from random import randint

while True:
    player = input('choose rock, paper or scissors')
    choice = ['rock', 'paper', 'scissors']
    computer = choice[randint(0, 2)]

    if player == 'quit':
        break

    elif player == computer:
        print('it\'s a tie!')
    elif player == 'rock':
        if computer == 'paper':
            print('you lose')
        else: print('you win!')
    elif player == 'paper':
        if computer == 'scissors':
            print('you lose')
        else: print('you win!')                    
    elif player == 'scissors':
        if computer == 'rock':
            print('you lose')
        else: print('you win')
    else: print('hey bozo, that is not a valid turn – check you\'re spelling')    



#   while True: 
#     usr_command = input("Enter your command: ")
#     if usr_command == "quit":
#       break
#     else: 
#       print("You typed " + usr_command)