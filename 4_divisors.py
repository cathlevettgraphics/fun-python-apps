# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


user_input = int(input('give me a number :)'))
divisor = range(1, user_input) 
output=[]

for num in divisor:
  if user_input % num == 0:
    output.append(num)
print(output)