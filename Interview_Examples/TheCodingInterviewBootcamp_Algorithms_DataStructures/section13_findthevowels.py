"""

Write a function that returns the number of vowels
used in a string.
Vowels are the characters: a, e, i, o , u

Examples:

    vowels("Hi there!") -> 3
    vowels("Why do u ask?" -> 4
    vowels("Why?) -> 0
"""


def vowels(sentence):
    dictionary_of_vowels = {}

    #we lower case the sentence, so we do not skip the big letters as well!
    sentence = sentence.lower()

    #checker = [a, e, i, o, u]

    for char in sentence:
        #if char in checker:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            if char not in dictionary_of_vowels:
                dictionary_of_vowels[char] = 1
            else:
                dictionary_of_vowels[char] += 1

    print(dictionary_of_vowels)

    number_of_vowels = 0
    for char in dictionary_of_vowels:
        number_of_vowels = number_of_vowels + dictionary_of_vowels[char]

    result = number_of_vowels
    return result

if __name__ == "__main__":

    example = "ddddddddddddddddddd"
    print(vowels(example))

