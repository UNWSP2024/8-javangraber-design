# Programmer: Javan Graber
# Date: 3/18/26
# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."
# Then ask the user for a subject (like "COS").
# Finally, the program will display the ID and name of all the courses having that subject.

def create_list_dictionary():
    # Create a constant
    again = "y"

    # Create an empty list and dictionary
    full_course_dict = {}
    full_list = []

    # Create a loop
    while again == "y":
        # Create an internal list
        internal_list = []
        # Find all the course information and add it to the mini list
        course_identity = str(input("Enter the first three letters of the course (in capitals): "))
        internal_list.append(course_identity)

        course_identity_number = str(input("Enter the numbers of the course ID: "))
        internal_list.append(course_identity_number)

        course_name = str(input("Enter the name of the course: "))
        internal_list.append(course_name)

        # Add the mini list ot the full list
        full_list.append(internal_list)
        # Add the all information to the dictionary
        full_course_dict[course_identity + course_identity_number] = course_name
        # Ask if there is another course
        again = str(input("Would you like to add another course (y/n): "))


    return full_list, full_course_dict


def find_needed_courses(full_list):
    # Create an empty course list
    selected_courses = []
    # Ask for the selected course type
    selection = str(input("Enter the type of course by typing the first three letters as capitals: "))

    # Create a loop that iterates over the full list
    for row in full_list:
        if row[0] == selection:
            # Add the two parts to create the whole ID
            course_needed = row[0] + row[1]
            # Add it to the list
            selected_courses.append(course_needed)

    return selected_courses

def main():
    # Call the create_list_dictionary function for the full list and course dictionary
    full_list, full_course_dict = create_list_dictionary()

    # Call the find_needed_course function for the selected courses list
    selected_courses = find_needed_courses(full_list)

    # Create the final dictionary
    new_full_course_dictionary = {}

    # Create a loop that matches the selected course list and the dictionary
    for key in full_course_dict.keys():
        if key in selected_courses:
            new_full_course_dictionary[key] = full_course_dict[key]

    # Give the courses that meet the requirements
    print("Here are the courses that meet the requirements you gave:")
    for key, value in new_full_course_dictionary.items():
        print(key, value)


# Call the main function
if __name__ == '__main__':
    main()

