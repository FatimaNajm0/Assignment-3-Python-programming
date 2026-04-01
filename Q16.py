# Import the random module to be able to generate random numbers
import random

# Define the main function that will run the guessing game
def play_guessing_game():
    # Generate a random integer between 1 and 100 (inclusive)
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a secret number between 1 and 100.")
    
    # Start a continuous loop that will keep asking for guesses
    while True:
        # Prompt the user for a guess and convert the input string to an integer
        guess = int(input("Enter your guess: "))
        
        # Check if the user's guess is higher than the secret number
        if guess > secret_number:
            print("Too high! Try again.")
            
        # Check if the user's guess is lower than the secret number
        elif guess < secret_number:
            print("Too low! Try again.")
            
        # If it's not higher and not lower, it must be the exact match!
        else:
            print("Congratulations! You guessed the correct number.")
            # Break out of the while loop to end the game
            break

# Call the function to start playing
play_guessing_game()
