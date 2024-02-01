# Quiz project
'''In this project we will ask the user say 10(here doing only 4 questions) questions and on the basis of the answer score will be given 
+1 for right answer and 0 for wrong answer and then we will display the total score of the users'''
print("Welcome to the Resident Evil Quiz")
playing=input("Do you want to play the game? ")

if playing.lower()!="yes":
    quit()
print("Okay! Let's go :)")
score=0
ans=input("Chris Redfield's sister is : ")
if ans.lower()=="claire redfield":
    print("Correct")# Can add a little more to the correct string
    score+=1
else:
    print("Incorrect")# Can add a little bedazzle
ans=input("Who was the protagonist in RE4 : ")
if ans.lower()=="leon":
    print("Correct")
    score+=1
else:
    print("Incorrect")
ans=input("Claire Redfield and Leon first met in which RE part(number only) : ")
if ans.lower()=="2":
    print("Correct")
    score+=1
else:
    print("Incorrect")
ans=input("Carlos appears in which RE (Number only): ")
if ans.lower()=="3":
    print("Correct")
    score+=1
else:
    print("Incorrect")
print(f"Your total score is {score}")
per=(score*100)/4
print(f"You answered {per} of the questions")
# You can also ask the user the number of question that is going to be in the quiz