# Imports / Modules
import random as rd

# Loop Condition - To Make Program keep running
#   To Be able to try again if the user looses
running = True

# Program Loop
while running :

    # The Computer chooses the Right Number
    #   randomly between 1 and 100
    right_number = int(rd.uniform(0, 100))

    # Then 2 Wrong Number
    #   randomly between 1 and 100
    wrong_number_1 = int(rd.uniform(0, 100))
    wrong_number_2 = int(rd.uniform(0, 100))

    # Store the Numbers in A List
    numbers = [right_number, wrong_number_1, wrong_number_2]

    # Define Number List As A Hint for the User
    numbers.sort()

    # Ask the User to choose a Number
    user_input = int(input(f'Choose a Number {numbers[0]} , {numbers[1]}, {numbers[2]} : '))

    # Try again if number isn't in list
    while user_input not in numbers:

        # Loop Try Again until the number typed is in the list
        user_input = int(input(f'Number not in List ! Try Again ! Choose a Number {numbers[0]} , {numbers[1]}, {numbers[2]} : '))
        continue

    # Check If the Number Belongs to the range
    if user_input in numbers:

        # Print A Message !
        print(f'The Number {user_input} belongs to the List')

        # Check if the user Typed the right Number
        if user_input == right_number:

            # The User Won the Game
            print('Congratulations ! You have won the Game !')
            running = False
            break

        else :

            # The Use Lose
            print(f'Sorry ! The Right Number was {right_number}')

            # Retry the Game ? Y / O
            user_retry = input('Retry the Game ? Y/N  :   ')

            while user_retry != 'Y' and user_retry != 'N':

                # In Failure Retrying , Please retype Y / N
                print('Please Type \'Y\' to retry the Game or \'O\' to quit    :   ')

                user_retry = input('Retry the Game ? Y/N  :   ')

            # If The User wants to retry
            if user_retry == 'Y':

                # Show Print + Retry
                print('Game has been Reset !')
                continue

            else:

                # Show Print + Close Game
                print('Closing the Game')
                running = False
                break
