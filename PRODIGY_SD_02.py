import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("I have chosen a number between 1 and 100. Try to guess it!")

    while True:
        # User inputs their guess
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        # Increment the attempt counter
        attempts += 1

        # Compare the guess to the number and provide feedback
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

# Run the game
guess_the_number()

