import sys
from random import randint

# Values are to be set as follows:
# Rock      1
# Paper     2
# Scissors  3
# Lizard    4
# Mr.Spock  5

def FingerBattle(userFinger,compFinger):
    #compFinger = randint[1,5]
    if userFinger == 1:     #Rock
        if compFinger == 1:
            return "Your opponent also throw Rock. Tie!"
        elif compFinger == 2:
            return "Your opponent throw Paper. Paper covers Rock. You lose!"
        elif compFinger == 3:
            return "Your opponent throw Scissors. Rock destroy Scissors. You win!"
        elif compFinger == 4:
            return "Your opponent throw Lizard. Rock crushes Lizard. You win!"
        elif compFinger == 5:
            return "Your opponent throw Mr.Spock, and he vaporizes Rock. You lose!"

    if userFinger == 2:     #Paper
        if compFinger == 1:
            return "Your opponent throw Rock. Paper covers Rock. You win!"
        elif compFinger == 2:
            return "Your opponent also throw Paper. Tie!"
        elif compFinger == 3:
            return "Your opponent throw Scissors. Scissors cut Paper. You lose!"
        elif compFinger == 4:
            return "Your opponent throw Lizard, and it eats the Paper. You lose!"
        elif compFinger == 5:
            return "Your opponent throw Mr.Spock. The Paper disapproves him. You win!"

    if userFinger == 3:     #Scissors
        if compFinger == 1:
            return "Your opponent throw Rock. Rock destroy Scissors. You lose!"
        elif compFinger == 2:
            return "Your opponent also throw Paper. Scissors cut Paper. You win!"
        elif compFinger == 3:
            return "Your opponent also throw Scissors. Tie!"
        elif compFinger == 4:
            return "Your opponent throw Lizard. Scissors decapitate Lizard. You win!"
        elif compFinger == 5:
            return "Your opponent throw Mr.Spock, and he smashes your Scissor. You lose!"

    if userFinger == 4:     #Lizard
        if compFinger == 1:
            return "Your opponent throw Rock. Rock crushes Lizard. You win!"
        elif compFinger == 2:
            return "Your opponent throw Paper. Lizard eats the Paper. You win!"
        elif compFinger == 3:
            return "Your opponent throw Scissors. Scissors decapitate Lizard. You lose!"
        elif compFinger == 4:
            return "Your opponent also throw Lizard. Tie!"
        elif compFinger == 5:
            return "Your opponent throw Mr.Spock, and the Lizard poisons Mr.Spock. You win!"

    else:
    #if userFinger == 5:     #Mr.Spock
        if compFinger == 1:
            return "Your opponent throw Rock. Mr.Spock vaporizes Rock. You win!"
        elif compFinger == 2:
            return "Your opponent throw Paper. The Paper disapproves Mr.Spock. You lose!"
        elif compFinger == 3:
            return "Your opponent throw Scissors. Mr.Spock smashes Scissor. You win!"
        elif compFinger == 4:
            return "Your opponent throw Lizard, and the Lizard poisons Mr.Spock. You lose!"
        elif compFinger == 5:
            return "Your opponent also throw Mr.Spock. Tie!"



print("Welcome to the Rock Paper Scissors Lizard Spock challenge!")
print("Fight the computer! Now choose your finger figure:")

while (True):
    print ("1. Rock")
    print ("2. Paper")
    print ("3. Scissors")
    print ("4. Lizard")
    print ("5. Mr.Spock")
    print ("6. I don't want to play..")
    userFinger = input("    Enter your number of choice: ")
    userFinger = int(userFinger)

    if userFinger == 6:
        print ("Bye!")
        exit(0)
    if (userFinger > 0) and (userFinger < 6):
        compFinger = randint(1,5)
        result = FingerBattle(userFinger,compFinger)
        print(" ")
        print(" ")
        print(result)
        print(" ")
        print(" ")
    else:
        print(" ")
        print(" ")
        print ("Not a valid choice!")
        print(" ")
        print(" ")

