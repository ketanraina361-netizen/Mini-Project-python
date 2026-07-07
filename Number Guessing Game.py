import random
#Computer choose a random number
number = random.randint(1, 10)

attempts = 0

while True:
    guess = int(input("Enter your guess (1-10): "))
    attempts += 1

    if guess > number:
        print("Too High!")
    elif guess < number:
        print("Too Low!")
    else:
        print("Correct! You guessed it.")
        print("Attempts:", attempts)
        break