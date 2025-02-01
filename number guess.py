import random

lowest_num = 1
highest_num = 20
awnser = random.randint(lowest_num, highest_num)
guesses = 0
running = True

print(f"this is a number guessing game, guess a number between {lowest_num} and {highest_num}")

while running:
    guess = int(input("enter your guess:"))
    if guess == "0":
        guess = int(guess)
        guesses += 1
    else:
        guess = int(guess)
        guesses += 1
    if guess == awnser:
        print(f"you got it! the awnser was {awnser}")
        print(f"you guessed {guesses} times")
        running = False
    elif guess < awnser:
        print("to low, try again")
    elif guess > awnser:
        print("to high, try again")
