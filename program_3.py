# Programmer: Javan Graber
# Date: 3/18/2026
# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys,
# and their capitals as values.
# The program should then randomly quiz the user by displaying the name of a state
# and asking the user to enter the state's capital.
# The program should count of the number of correct and incorrect responses.
# (You could alternatively use another country and provinces,
# or countries of the world and capitals).
import random

def main():
    state_capital_dictionary = {'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
'Hawaii': 'Honolulu',
'Idaho': 'Boise',
'Illinois': 'Springfield',
'Indiana': 'Indianapolis',
'Iowa': 'Des Moines',
'Kansas': 'Topeka',
'Kentucky': 'Frankfort',
'Louisiana': 'Baton Rouge',
'Maine': 'Augusta',
'Maryland': 'Annapolis',
'Massachusetts': 'Boston',
'Michigan': 'Lansing',
'Minnesota': 'Saint Paul',
'Mississippi': 'Jackson',
'Missouri': 'Jefferson City',
'Montana': 'Helena',
'Nebraska': 'Lincoln',
'Nevada': 'Carson City',
'New Hampshire':  'Concord',
'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe',
'New York': 'Albany',
'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck',
'Ohio': 'Columbus',
'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem',
'Pennsylvania': 'Harrisburg',
'Rhode Island': 'Providence',
'South Carolina': 'Columbia',
'South Dakota': 'Pierre',
'Tennessee': 'Nashville',
'Texas': 'Austin',
'Utah': 'Salt Lake City',
'Vermont': 'Montpelier',
'Virginia': 'Richmond',
'Washington': 'Olympia',
'West Virginia': 'Charleston',
'Wisconsin': 'Madison',
'Wyoming': 'Cheyenne'}


    # Create a constant for again, the number of correct answers, the incorrect answers,
    # and the loop number
    again = True
    correct = 0
    incorrect = 0
    loop = 0

    # Create the loop that will quiz the user
    while again != False and loop != 50:

        # Get the selection from the loop
        random_selection = select_random_states(state_capital_dictionary)

        # Find the correct answer
        correct_answer = state_capital_dictionary[random_selection]

        # Ask the user for the answer
        user_answer = str(input(f'Enter the capital of {random_selection} or type stop to end: '))

        # Create the loop that checks each possibility for the user answer
        if user_answer == correct_answer:
            print("That is correct!")
            again = True
            correct += 1
        elif user_answer == "stop":
            print(f"Your were correct on {correct} and incorrect on {incorrect}.")
            again = False
        elif user_answer != correct_answer:
            print(f"Sorry, {correct_answer} is the actual capital of {random_selection}.")
            incorrect += 1
            again = True
        else:
            print('An error occurred.')

            # Pop the selection from the list
            state_capital_dictionary.pop(random_selection)

        # Give the loop amount
        loop += 1

def select_random_states(state_capital_dictionary):
    # Create a list of all the keys
    selection_keys = list(state_capital_dictionary.keys())

    # Randomly select a key
    random_selection = random.choice(selection_keys)



    return random_selection

# Call main
if __name__=="__main__":
    main()
