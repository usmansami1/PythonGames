import random
# Start of the game with rules and guidelines
print("""=====================================================================================================
                                    !---- Welcome to Number Guessing Game ----!
=====================================================================================================""")
print("""RULES:
                1) Computer will generate a random number from 1 to 100
                2) A player can enter his guess
                3) Based on that guessed number, hints will be given like too big or too small for difference of 10 or more
                   Close will be given in case of difference less than 10 
                4) There are no limits for guesses
                5) Total number of guesses will be shown at the end""")
line = "_"*100
print(line)
number = random.randint(1,100)
print("The number has been generated. Lets play the game!")
winning = True
guess = 0
while(winning):
    try:
        num = int(input("Enter your number : "))
    except ValueError:
        print("Please enter a valid number.")
    if num<1 or num>100:
        print("Please enter a number between 1 and 100.")
        continue
    difference = abs(num-number)
    if(num == number):
        guess+=1
        print("Congrats you have guessed correctly!")
        print("The number of guesses used are",guess)
        line = "_"*100
        print(line)
        winning = False
        break
    elif (num > number and difference >= 10):
        print("The guessed number is too big!")
        print(line)
        guess+=1

    elif (difference < 10):
        print("The guessed number is close!\nYou are in the right direction")
        print(line)
        guess+=1

    elif (num < number and difference >= 10):
        print("The guessed number is too small!")
        print(line)
        guess+=1
   
    
    
