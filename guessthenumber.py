import random
import time

print("Guess a number game!")
time.sleep(1)
print("Rules:")
print("You choose a number between something and something, and try guessing it!")
time.sleep(4)
print()

fails = int(input("Choose attempts number: "))
number1 = int(input("Choose generate number from: "))
number2 = int(input("To: "))
print("You chose")
print(fails, "Fails")
print("Random number from", number1)
print("To", number2)

rightorno = input("Is that right? yes/no ")

if rightorno == 'yes' or 'Yes':
    print("Game starts!")
elif rightorno == 'no' or 'No':
    print("Exitting the game :(")
    exit()
#Generates a random number from number1 to number2

RandomNumber = random.randint(number1, number2)
global FailsCounter
FailsCounter = 0


#If RandomNumber is even make the variable Even if else, Odd

EvenOrNot = 0

if RandomNumber %2 == 0:
    EvenOrNot = 1
else:
    EvenOrNot = 2




def Guess():
    Guess = int(input("Your guess: "))
    global FailsCounter
    if FailsCounter == fails:
        print("You lost!")
        print("The number was", RandomNumber)
        exit()

    if Guess == RandomNumber:
        print("You won!")
        time.sleep(5)
        exit()
    else:
        FailsCounter = FailsCounter + 1

        print("You lost. Try again.", FailsCounter, "out of ", fails)
        
        if EvenOrNot == 1:
            print("The number is Even")
            Guess2()
        else:
            print("Hint: The number is odd.")
            Guess2()

def Guess2():
    Guess2 = int(input("Your guess: "))
    global FailsCounter
    if FailsCounter > fails:
        print("You lost!")
        print("The number was", RandomNumber)
        exit()
    
    if Guess == RandomNumber:
        print("You won!")
        time.sleep(5)
        exit()
    else:
        FailsCounter = FailsCounter + 1
        print("You lost. Try again.", FailsCounter, "out of ", fails)
        
        if EvenOrNot == 1:
            print("Hint: The number is Even.")
            Guess()
        else:
            print("Hint: The number is odd.")
            Guess()
#call Guess() To play the game
Guess()
