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
    wrong_number_1 = int(rd.uniform(0, 50))
    wrong_number_2 = int(rd.uniform(50, 100))

    # Store the Numbers in A List
    numbers = [right_number, wrong_number_1, wrong_number_2]

    # Define Number Range As A Hint for the User
    number_range = range(min(numbers), max(numbers) + 1)

    # Ask the User to choose a Number
    user_input = int(input(f'Choose a Number between {min(numbers)} and {max(numbers)} : '))

    # Try again if number isnt in range
    while user_input not in number_range:

        #
        user_input = int(input(f'Number not in range ! Try Again ! Choose a Number between {min(numbers)} and {max(numbers)} : '))
        continue

    # Check If the Number Belongs to the range
    if user_input in number_range:

        #
        print(f'The Number {user_input} belongs to the range')

        #
        if user_input == right_number:

            #
            print('Congratulations ! You have won the Game !')
            running = False
            break

        else :

            #
            print(f'Sorry ! The Right Number was {right_number}')

            #
            user_retry = input('Retry the Game ? Y/O  :   ')

            while user_retry != 'Y' and user_retry != 'O':

                #
                print('Please Type \'Y\' to retry the Game or \'O\' to quit    :   ')

                #
                user_retry = input('Retry the Game ? Y/O  :   ')

            #
            if user_retry == 'Y':

                #
                print('Game has been Reset !')
                continue

            else:

                #
                print('Closing the Game')
                running = False
                break
