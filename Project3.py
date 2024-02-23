'''This project is rock, paper and scissors. We will keep scores of who wins the most.It is user v/s CPu'''
import random
user_wins=0
comp_wins=0
options=["rock","paper","scissors"]
while True:
    user_input=input("Choose Rock, paper or scissors or Q to quit: ").lower()
    if user_input=="q":
        break
    elif user_input not in options:
        continue
    # 0 is for rock, 1 is for paper and 2 is for scissors
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print(f"Computer picked {computer_pick}")
    if user_input=="rock" and computer_pick=="scissors":
        print("You won!")
        user_wins+=1
    elif user_input=="paper" and computer_pick=="rock":
        print("you won!")
        user_wins+=1
    elif user_input=="scissors" and computer_pick=="paper":
        print("you won!")
        user_wins+=1
    elif user_input=="paper" and computer_pick=="paper":
        print("draw")
    elif user_input=="rock" and computer_pick=="rock":
        print("draw")
    elif user_input=="scissors" and computer_pick=="scissors":
        print("draw")
    else:
        print("Computer wins. Better luck next time.")
        comp_wins+=1
if user_wins>comp_wins:
    print(f"You won with a total score of {user_wins}")
else:
    print(f"Computer won with total score of {comp_wins}")
print("goodbye!")
