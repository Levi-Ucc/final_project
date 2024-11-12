import random

# Generate a random number between 1 and 10
number_to_guess = random.randint(1, 100)

# Explain the game to the player
print("Welcome to the Guess the Number game!")
print("I have chosen a number between 1 and 10.")
print("Can you guess what it is?")

# Initialize the player's guess
guess = None

# Loop until the player guesses the correct number
while guess != number_to_guess:
    # Ask the player for their guess
    guess = int(input("Enter your guess: "))

    # Check if the guess is too low, too high, or correct
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")

# End of the game
print("Thanks for playing!")
