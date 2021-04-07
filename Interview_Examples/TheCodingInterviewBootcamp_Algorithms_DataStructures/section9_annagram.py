"""
Check to see if two provided strings are anagrams of each other.
One string is an anagram of another if it uses the same characters
in the same quantity.
Only consider characters, not spaces or punctuation
Consider letters to be the same as lower cases

-- Examples:
anagrams('rail safety', 'fairy tales') True
anagrams('Rail! SAFETY', 'fairy tales') -- True
anagrams('Hi there', 'Bye there') --> false

"""

"""

The Python isalpha() method returns true if a string only contains letters.
Python isnumeric() returns true if all characters in a string are numbers.
Python isalnum() only returns true if a string contains alphanumeric characters, without symbols.
"""

def anagrams(string_a, string_b):
    string_b = string_b
    string_a = string_a
    string_a_clean = ""

    #print("is string a lower", string_a.islower()) -- > False

    print(string_a.isalpha())
    #string_a.lower()
    #print("is string a lower", string_a.islower())
    string_a = string_a.lower()
    #print("is string a lower", string_a.islower())
    print("string a:", string_a)
    for char in string_a:
        if char.isalnum():
            print(char)
            string_a_clean = string_a_clean + char

    print(string_a_clean)

    string_b_clean = ""
    string_b = string_b.lower()
    for char in string_b:
        if char.isalnum():
            string_b_clean+= char

    print("string a to compare", string_a_clean, "string b to compare", string_b_clean)

    dictionary_of_chars_string_a = {}
    dictionary_of_chars_string_b = {}
    for char in string_a_clean:
        if char not in dictionary_of_chars_string_a:
            dictionary_of_chars_string_a[char] = 1
        else:
            dictionary_of_chars_string_a[char] += 1

    print("chars in string a", dictionary_of_chars_string_a)
    print("keys in string a", dictionary_of_chars_string_a.keys())
    #print("items in string a", dictionary_of_chars_string_a.items())

    for char in string_b_clean:
        if char not in dictionary_of_chars_string_b:
            dictionary_of_chars_string_b[char] = 1
        else:
            dictionary_of_chars_string_b[char] += 1
    print("chars in string b", dictionary_of_chars_string_b)
    print("keys in string b", dictionary_of_chars_string_b.keys())

    #checking it those are anagrams
    #1) we must have the same number of keys in the dictionaries
    if (len(dictionary_of_chars_string_a.keys())) != (len(dictionary_of_chars_string_b.keys())):
        return False

    # 2) we must have the same values in the same keys
    for key in dictionary_of_chars_string_a:
        if dictionary_of_chars_string_a[key] == dictionary_of_chars_string_b[key]:
            return True
        else:
            return False



if __name__ == "__main__":

    result = anagrams("!! kayak", "KAYAK !!!!")
    print(result)