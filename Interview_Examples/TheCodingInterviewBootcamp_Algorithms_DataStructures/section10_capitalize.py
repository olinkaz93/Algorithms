"""
Write the function that accepts a string.
The function should capitalize the first letter of each word
in the string then return the capitalized string.
---
examples:
capitalize("a short sentence") -> "A Short Sentence"
capitalize("look, it's working!") --> 'Look, It is Working!"

"""

def capitalize(string):

    new_string = ""
    index_before_character = None
    for index_of_character in range(0, len(string), 1):
        if index_of_character == 0:
            upper_char = string[index_of_character].upper()
            new_string = new_string + upper_char
            #index_before_character = index_of_character
        elif string[index_before_character] == " " and string[index_of_character].isalpha():
            upper_char = string[index_of_character].upper()
            new_string = new_string + upper_char
            #index_before_character = index_of_character
        else:
            new_string = new_string + string[index_of_character]
        index_before_character = index_of_character


    return new_string

if __name__ == "__main__":
    word = "         jak sie masz ??? ddd ?? dd ?"
    result = capitalize(word)
    print(result)


