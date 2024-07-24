# This project is quiz game
score=0
player_name=input("Your name: ")
print("Welcome,",player_name.title())
instructions=input("Do you wnat intrustions for the game: Y/N\n")
if instructions.lower()=="y":
    print("The games has the following rules:")
    print("1) For every correct answer teh player will be rewarded with a +1")
    print("2) For every wrong answer the player's score will be deducted by -1")
    print("3)For skipping the(which is done by typing 'skip') answer the player will be given 0")

ques_1=input("What is the capital of Italy?\n")
if ques_1.lower()=="rome":
    print("Correct answer")
    score=score+1
elif ques_1.lower()=="skip":
    print("the answer has been skipped")
    score=score+0
else:
    print("Wrong answer")
    print("The correct answer is : Rome")
    score=score-1
    print("You have not answered the question")
ques_2=input("What is the longest river in the world? \n")
if ques_2.lower()=="nile":
    print("Correct answer")
    score=score+1
elif ques_2.lower()=="skip":
    print("the answer has been skipped")
    score=score+0
else:
    print("The correct answer is Nile")
    score=score-1
ques_3=input("What does WHO stand for ?\n")
if ques_3.lower()=="world health organization":
    print("Correct answer")
    score=score+1
elif ques_3.lower()=="skip":
    print("the answer has been skipped")
    score=score+0
else:
    print("the correct answer is World Health Organiztion")
    score=score-1
ques_4=input("How many bones are there in the human body?\n")
if ques_4=="206":
    print("Correct answer")
    score=score+1
elif ques_4.lower()=="skip":
    print("the answer has been skipped")
    score=score+0
else:
    print("The correct answer is 206")
    score=score-1
ques_5=input("What is the currency of Japan?\n")
if ques_5.lower()=="yen":
    print("Correct answer")
    score=score+1
elif ques_5.lower()=="skip":
    print("the answer has been skipped")
    score=score+0
else:
    print("The corret answer is Yen")
    score=score-1
total_score=score
print("Your total score is:",total_score)

