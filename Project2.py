'''In this project we will track how many numbers does the user guess correctly using a random number generator and giving 1 for correct
guess and 0 for the wrong guess'''

import random
top_of_range=input("Type a number: ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range <= 0:#Not working
        print("Please enter a number greater than 0")
        quit()
else:
    print("Please enter a number next time")
    quit()
num=random.randint(0,top_of_range)
guesses=0
# print(f"Random number = {num}")
while True:
    guesses+=1
    user_guess=input("take a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Enter a number next time!!")
        continue
    if user_guess==num:
        print("You got it!!")
        break
    elif user_guess>num:
        print(f"Your guess was above the number")
    else:
        print(f"Your guess is below the number")
print(f"Number of guesses = {guesses}")