### Part Two -- your code goes here. 
import random

x = random.randint(1,100)
y = None

print("Welcome to the Number guessing game!")
print("I'm thinking of a number between 1 and 100. Please guess what it is!!")

while y != x:
    y = int(input("Enter your guess number: "))
    
    if y < x:
        print("It is too low. Please try again!")
    elif y > x:
        print("It is too high. Please try again!")
    else:
        print(f"Congratulation!! You got it!! {y}: ")
