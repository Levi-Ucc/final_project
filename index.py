import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Explain the game to the player
print("Welcome to the Guess the Number game!")
print("I have chosen a number between 1 and 100.")
print("Can you guess what it is? You have 5 attempts.")

# Initialize the player's guess and attempt counter
guess = None
attempts = 0
max_attempts = 5

# Loop until the player guesses the correct number or runs out of attempts
while guess != number_to_guess and attempts < max_attempts:
    # Ask the player for their guess
    guess = int(input("Enter your guess: "))
    attempts += 1

    # Check if the guess is too low, too high, or correct
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")

    # Check if the player has used all attempts
    if attempts == max_attempts and guess != number_to_guess:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

# End of the game
print("Thanks for playing!")