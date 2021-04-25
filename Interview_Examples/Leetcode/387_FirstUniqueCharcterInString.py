def firstUnique(word):

    dictionary_of_characters = {}

    for index, char in enumerate(word):
        if char not in dictionary_of_characters:
            dictionary_of_characters[char] = [index]
        else:
            dictionary_of_characters[char].append(index)


    print(dictionary_of_characters)

    for char in dictionary_of_characters:
        print(char, " ", len(dictionary_of_characters[char]))
        if (len(dictionary_of_characters[char])) == 1:
            print(char, "at index", dictionary_of_characters[char][0])
            return

def firstUnique2(word):
    from collections import OrderedDict

    dictionary_of_characters = OrderedDict()
    #dictionary_of_characters = {}

    for index, char in enumerate(word):
        current_unique = char
        if char not in dictionary_of_characters:
            dictionary_of_characters[char] = [index]
            first_unique = char
        else:
            dictionary_of_characters[char].append(index)



    print(dictionary_of_characters)

    for char, indexes in dictionary_of_characters.items():
        print(char, " ", indexes)
        print("my indexesS!:", indexes)
        if (len(indexes)) == 1:
            print(indexes)
            return indexes[0]

    return -1



if __name__ == "__main__":
    word = "eetccdee"

    #result = firstUnique(word)
    #print(result)
    #result = firstUnique2(word)
    result = firstUnique2("loveleetcode")
    print(result)