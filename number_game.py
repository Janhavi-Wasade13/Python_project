import random

n = random.randint(1,100)

a =-1
guesses = 0
while(a != n):
    
    a = int(input("Guess a Number: "))
    if(a>n):
        print("Lower number please!")
        guesses += 1

    elif(a<n):
        print("Higher no. please")  
        guesses += 1  


print(f"You have guesses the no. correctly in {guesses} attempt")        


