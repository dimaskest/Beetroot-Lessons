import random


x = int(input("Guess the number from 1 to 10: "))
random_x = random.randint(1, 10)

if x == random_x:
    print("Congratulations, you guessed a number!")
else:
    print(f"The number was {random_x}, better luck next time!")
