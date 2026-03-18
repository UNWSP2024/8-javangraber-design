# Programmer: Javan Graber
# Date: 3/15/2026
# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all the words are run together,
# but the first character of each word is uppercase.
# Convert the sentence to a string in which the words are separated by spaces,
# and the first word starts with an uppercase.
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

def main():
    # Create a variable sentence
    new_sentence = ""

    # Ask for the sentence
    sentence = str(input("Enter the sentence: "))

    # Call for the function to get the new sentence
    changed_sentence = word_separator(sentence, new_sentence)

    # Print the new sentence
    print(changed_sentence)

def word_separator(sentence, new_sentence):

    # Get the first letter into the new sentence
    new_sentence = new_sentence + sentence[0]

    for char in range(1, len(sentence)):

        char = sentence[char]

        # Test each character within the loop
        if char.isupper():
            char = char.lower()
            new_sentence = new_sentence + " "

        new_sentence = new_sentence + char

    return new_sentence.strip()

# Example usage
if __name__=="__main__":
    main()
