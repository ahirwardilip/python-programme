#Number Guessing Game
import random
print("Number Guessing Game")

number = random.randint(0,100)
#print("random",number)
chances = 0
print("Guess the number (between 0 and 100):")

while chances < 5:
    guess = int(input())
    if guess == number:
        print("congratulation")
        break
    elif guess < number:
        print("your guess was too low: guess a number higher than",guess)
    else:
        print("your guess was too high: guess the number lower than",guess)

    chances += 1
    if not chances <5:
       print("you loose",number)           
