import random

low = 0
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Enter a number between ({low} - {high}): "))
    guesses += 1

    if guess < number:
        print(f"{guess} NO IT Too LOW")
    elif guess > number:
        print(f"{guess} No IT Too HIGH")
    else:
        print(f"{guess} You Got WIN")
        break

print(f"This round took you {guesses} Wrong Guesses")