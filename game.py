import random
'''
1 for snake
0 for gun
-1 for water

'''
computer = random.choice([-1,0,1])         #possibilities are 0, 1, -1

youstr = input("Enter your choice: ")
youDict = {"s" : 1,"w": -1,"g": 0}
reverseDict = { 1 : "Snake", -1: "Water",0 :"Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose:{reverseDict[computer]}")

if(computer == you):
   print("Its's a draw")
    
else: 
    if(computer == -1 and you == 1):
        print("You win!")


    elif(computer == 1 and you == -1):
        print("You Lose!")  

    elif(computer == 0 and you == 1):
        print("You Lose!")

    elif(computer == 1 and you == 0):
        print("You Win!")        

    elif(computer == -1 and you == 0):
        print("You Lose!")

    elif(computer == 0 and you == -1):
        print("You Win!")  

    else:
        print("Something went wrong")     



# or
# import random

# print("Welcome to Snake Water Gun Game")

# choices = ["snake", "water", "gun"]

# # Computer choice
# computer = random.choice(choices)

# # User choice
# user = input("Enter your choice (snake/water/gun): ").lower()

# print("Computer chose:", computer)
# print("You chose:", user)

# # Game logic
# if user == computer:
#     print("It's a draw!")

# elif (user == "snake" and computer == "water"):
#     print("You win! Snake drinks water.")

# elif (user == "water" and computer == "gun"):
#     print("You win! Water damages gun.")

# elif (user == "gun" and computer == "snake"):
#     print("You win! Gun kills snake.")

# elif user in choices:
#     print("Computer wins!")

# else:
#     print("Invalid input! Please choose snake, water, or gun.")