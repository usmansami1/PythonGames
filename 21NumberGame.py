import random
# Start of the game with rules and guidelines
print("""=====================================================================================================
                                    !---- Welcome to 21 Game ----!
=====================================================================================================""")
print("""RULES:
                1) Two players get turn one by one
                2) A player can choose to enter 1 to 3 numbers
                3) Numbers start from 1 and continue upwards
                4) The numbers entered by player must be consecutive
                5) The one who enters 21 loses the game!""")
print("_______________________________________________________________________________________________________\n")

# Allows user to choose wether he wants to play with computer or another player
choice = int(input("Enter 1 if you want to play with computer else enter 0 : "))

# Taking credentials for making smooth workflow of game
player1 = input("Enter the name of player 1 : ")
player2 = None
if choice == 0 :
    player2 = input("Enter the name of player 2 : ")

    # Here i am using random function so that first turn comes randomly
    player = random.choice([player1 , player2])
elif choice == 1 :
    player = random.choice([player1 , "Computer"])

numbersPresent = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
numbersUsed = []
winningCondition = True
def gameWorkflowForPlayers(player):
        print(f"The turn is of {player}")
        numberCountCheck = True
        while(numberCountCheck):

# handling edge last cases to prevent some errors
            if(len(numbersPresent)==1):
                howManyNumbers=1
            elif(len(numbersPresent)==2):
                howManyNumbers=2
            else:
                howManyNumbers = int(input("How many numbers you want to enter : "))

# validating inputs so that rules of game are being followed
            if (howManyNumbers>=1 and howManyNumbers<=3):
                numberCountCheck = False
            else:
                print("Invalid Input! Only 1 to 3 Numbers are allowed to enter.")

# Taking input of numbers from the user with validation logic
        for i in range (1,howManyNumbers+1):
            numberCheck = True
            orderCheck = True
            while(numberCheck or orderCheck):
                num = int(input(f"Enter number {i}: "))
                if (num in numbersPresent):
                    numberCheck = False
                elif(num<=0 or num>21):
                    print("The number entered is out of range (1 to 21)")
                else:
                    print("The number is already used!")
                if (num == numbersPresent[0]):
                    numbersPresent.remove(num)
                    numbersUsed.append(num)
                    orderCheck = False
                elif(num != numbersPresent[0]):
                    print("The numbers should be consecutive and increasing. Skipping numbers is not allowed")

        print(numbersUsed)
        print(f"Numbers available are : {numbersPresent}")

while (winningCondition):
    # Game workflow for player 1
    if player == player1 :
        gameWorkflowForPlayers(player1)
        # switching players to change the turns
        if choice==1:
            player = "Computer"
        else:
            player = player2
        print("_______________________________________________________________________________________________\n")

# game workflow for player 2
    elif player == player2 :
        gameWorkflowForPlayers(player2)
        player = player1
        print("_______________________________________________________________________________________________\n")

# game workflow for computer
    elif player == "Computer":
        print(f"The turn is of {player}")
        if(len(numbersPresent)==1):
            howManyNumbers=1
        elif(len(numbersPresent)==2):
            howManyNumbers=2
        else:
            howManyNumbers = random.choice([1,2,3])
        print(f"The computer chose to enter {howManyNumbers} numbers.")
        for i in range (0,howManyNumbers):
            num = numbersPresent[0]
            print(f"The computer entered following number : {num}")
            numbersPresent.remove(num)
            numbersUsed.append(num)
        print(numbersUsed)
        print(f"Numbers available are : {numbersPresent}")
        player = player1
        print("_______________________________________________________________________________________________\n")

# Checking the winning condition
    if 21 in numbersUsed:
        print(f"{player} won the game!")
        winningCondition = False