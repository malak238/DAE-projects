import random
# It orients the user, gives the rules
def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
 
    # Here is the random number generator
    number_to_guess = random.randint(1, 100)   
    attempts = 0
    guessed = False

    # This is to check if the numbers are in range or not. It makes sure to add attempts every time you guess.
    while not guessed:
        try:
            user_guess = int(input("Take a guess: "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("Please guess a number within the range!")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()