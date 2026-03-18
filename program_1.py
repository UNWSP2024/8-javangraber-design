# Programmer: Javan Graber
# Date: 3/15/2026
# Program #1: Initials

# Create the main function
def main():
    # Get name
    persons_name = str(input("Enter your first, middle, and last name: "))

    # Call the initials function
    initials_generator(persons_name)

def initials_generator(persons_name):
    # Create a variable string
    string_variable = ''

    # Split the name given
    split_name = persons_name.split()

    # Create the loop that examines the strings
    for string in split_name:
        print(string[0].upper(), sep='', end='')
        print('.', sep = ' ', end = '')


# Call main
if __name__=="__main__":
    main()
