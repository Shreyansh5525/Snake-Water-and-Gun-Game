import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")

youDict = {"s":1, "w":-1, "g":0}
reverseDict= {1:"Snake", -1:"Water", 0:"Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")



if (computer == you):
    print("It's a tie!")

else:

    if (computer ==-1 and you ==1):
        print("You win!")
        
    elif (computer ==-1 and you ==0):
        print("You lose!")
        
    elif (computer ==1 and you ==-1):
        print("You lose!")
    
    elif(computer ==1 and you ==0):
        print("You win!")    
        
    elif(computer ==0 and you ==-1):
        print("You win!")
        
    elif(computer ==0 and you ==1):
        print("You lose!")
        
    else:
        print("Something went wrong!    ")
