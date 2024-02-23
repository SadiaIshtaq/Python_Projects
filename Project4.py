'''This project is choose your own adventure game
User Interactive game'''
#This game has the potential to expand...
name=input("Enter your name: ")
print(f"Welcome {name} to this adventure!!")
answer=input("You are on a dirt road. You have two options:Left or Right.Which way do you want to go: ").lower()
if answer== "right":
    print("You have selected the Right of the dirt road.")
    print("Now..")
    answer=input("You have reached a river. You can either walk around the river or you can go through the river via a boat.Please type walk or boat: ")
    if answer=="boat":
        print("You went with the boat option but there was a hole in the boat you didn't notice.")
        print("you drowned. :(")
    elif answer=="walk":
        print("You chose to walk around the river and you finally found the treasure.")
        print("you won!")
    else:
        print("Please enter a valid option!")
elif answer=="left":
    print("You have selected the Left of the dirt road.")
    print("Now..")
    answer=input("Ahead is a wobbly looking bridge.Do you want to cross the bridge or you want to go back to the dirt road. (cross/back)")
    if answer=="cross":
        print("Alas! The bridge collapsed and you are dead")
    elif answer=="back":
        print("You went back and never returned on this path never again with empty hand.")
    else:
        print("Please enter a valid option.")
else:
    print("Please enter a valid option")
print(f"It was a fun adventure to have with you {name}.")

