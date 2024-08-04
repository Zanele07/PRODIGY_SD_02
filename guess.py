import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Loop until the user guesses the number
    while not guessed_correctly:
        try:
            # Prompt the user for a guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Provide feedback
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
