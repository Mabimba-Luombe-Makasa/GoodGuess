import random


# Main function that allows guessing and generates random numbers.
def user_range():
    # Try-Except is an error handling that ensures user enters numbers for the range he wants
    try:
        option_a = int(input("Enter the lower bound of the range: "))
        option_b = int(input("Enter the upper bound of the range: "))

        # Error handling if user enters a smaller number in the lower bound
        if option_a >= option_b:
            print("Error: The upper bound must be greater than the lower bound.")
            return

        # Creates a random number from the range the user gives
        random_number = random.randint(option_a, option_b)
        user_selection = input("Enter your guess: ")

        # Checks if the user entered a number
        if user_selection.isdigit():
            # Changes selection from string to integer
            user_selection = int(user_selection)

            # Checks if user guess is he same as the random generated number then prints message
            if user_selection == random_number:
                print("Congratulations! You guessed the number correctly.")

            # If user enters a number out of the given range it will give error message
            elif user_selection > option_b or user_selection < option_a:
                print("Error: Your guess is out of the specified range.")

            # If user does get it correct a message is printed and the guessed number is given
            else:
                print("Sorry, you guessed wrong. The correct number was:", random_number)

        # Error handling if user doesn't enter a numerical character when guessing
        else:
            print("Error: Please enter a valid numerical character.")

    # Error handling if user doesn't enter a numerical character when entering the bounds
    except ValueError:
        print("Error: Please enter valid numbers.")


# Title and Subheading
print("WELCOME TO GOOD GUESS")
print("Have some fun trying to get the right guess...\n")

# While loop keeps the app continuously running until user inout to close.
while True:
    # User input for choosing to start or close the app
    user_option = input("Type START to begin, type EXIT to close app.\n")
    option_declaration = user_option.lower()

    # Runs main function
    if option_declaration == 'start':
        user_range()

    # Exits the app
    elif option_declaration == 'exit':
        print("Thank you for playing. Goodbye!")
        break

    # Error handling when user doesnt enter the right option.
    else:
        print("Error: Invalid input. Please type START to begin or EXIT to close the app.\n")
