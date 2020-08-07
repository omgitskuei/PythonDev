'''
Create a loop that asks the user to guess how many 'twinkies' there are.
Inside the loop, have an 'if' statement that checks the number.
Print the message 'Too few' or 'Too many' until the user guesses correctly.
'''

import random

correctGuess = bool(False);
answer = random.randint(0, 100)              # NOTE:Generate a random number between 1-100
while correctGuess == False:
    guess = input("What's your guess?");
    guess = int(guess);
    if(guess<answer):
        print("Too few");
    elif(guess>answer):
        print("Too many");
    else:
        print("Correct!");
        correctGuess = True;
print("Finished")
