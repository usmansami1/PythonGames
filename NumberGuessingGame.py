import random
# Start of the game with rules and guidelines
print("""=====================================================================================================
                                    !---- Welcome to Number Guessing Game ----!
=====================================================================================================""")
print("""RULES:
                1) Computer will generate a random number from 1 to 100
                2) A player can enter his guess
                3) Based on that guessed number, hints will be given like too big for >10, too small for <10 or close
                4) There are no limits for guesses
                5) Total number of guesses will be shown at the end""")
print("_______________________________________________________________________________________________________\n")
number = random.randint(1,100)
print("The number has been generated. Lets play the game!")
winning = True
guess = 0
while(winning):
    num = int(input("Enter your number : "))
    if(num == number):
        print("Congrats you have guessed correctly!")
        print("The number of guesses used are",guess)
        print("_______________________________________________________________________________________________________\n")

        winning = False
    if (num>number and (num-number)>=10):
        print("The guessed number is too big!")
        print("_______________________________________________________________________________________________________\n")
        guess+=1
    elif (num>number and (num-number)<10):
        print("The guessed number is close!\nYou are in the right direction")
        print("_______________________________________________________________________________________________________\n")
        guess+=1
    elif (num<number and (number-num)>=10):
        print("The guessed number is too small!")
        print("_______________________________________________________________________________________________________\n")
        guess+=1
    elif (num<number and (number-num)<10):
        print("The guessed number is close!\nYou are in the right direction")
        print("_______________________________________________________________________________________________________\n")
        guess+=1
    
    
