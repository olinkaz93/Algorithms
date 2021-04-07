#Given a string, return the character that is most commonly
#used in the string

#maxChar("abcccccccccccd") == "c"
#maxChar(apple 123111111") == "1"

#similar questions:
#	What is the most common character in the string
#	Does string A have the same characters as string B (is it anagram)
#	Does the given string have any repeated characters in it ?


def maxChar(string):
    dictionary_of_characters = {}

    print(len(dictionary_of_characters))

    for char in string:
        if char not in dictionary_of_characters:
            dictionary_of_characters[char] = 1
        else:
            dictionary_of_characters[char] +=1


    for key in dictionary_of_characters:
        print("char", key, " value:", dictionary_of_characters[key])

    #print(len(dictionary_of_characters))
    if len(dictionary_of_characters) == 0:
        print("nothing to say")
        return

    #print("finding the most repetitive character")

    else:
        current_max = 0
        for key in dictionary_of_characters:
            if dictionary_of_characters[key] > current_max:
                current_max = dictionary_of_characters[key]
                key_max = key
        print("the max element is! ", key_max, "value of", current_max)

        print(dictionary_of_characters)
        return key_max


if __name__ == "__main__":

    result = maxChar("sdfdfsdkjdsks33434999mmx")
    print(result)