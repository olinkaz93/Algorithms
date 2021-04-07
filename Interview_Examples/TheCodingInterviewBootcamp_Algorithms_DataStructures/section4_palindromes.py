#Given a string, return a true if the strong is a palindrome
#or false if is not
#Do include spaces and punctuation in determing
#if the string is a palindrome
#examples:
# -- palindrome("abba") === true
# -- palindrome("abcdef") === false

def palindrome(word, another_word):
    # palindrome is the same word that when reversed
    # has the same value
    reversed_string = ""
    print(len(word))
    for i in range(len(word)-1, -1, -1):
        print("i: ", word[i])
        reversed_string = reversed_string+word[i]

    print("initial input", word, " ", type(word))
    print("reversed string", reversed_string, " ", type(reversed_string))
    print(word == reversed_string)

    ### reverse with indexing
    another_word = another_word[-1::-1]
    print("word", word)
    print("word", another_word)
    #new_word = word[-1::-1]
    #print(new_word)
    if print(word == reversed_string):
        return True
    else:
        return False


if __name__ == "__main__":

    palindrome("mamam", "siemamamamamaa")

    """Slicing Strings
We can also call out a range of characters from the string.
Say we would like to just print the word Shark.
We can do so by creating a slice, which is a sequence of characters
within an original string.
With slices, we can call multiple character values by creating a range of index numbers
separated by a colon [x:y]:

print(ss[6:11])
 
Output
Shark
When constructing a slice, as in [6:11],
the first index number is where the slice starts (inclusive),
and the second index number is where the slice ends (exclusive),
which is why in our example above the range has to be the index number that would occur just after the string ends.

When slicing strings, we are creating a substring,
which is essentially a string that exists within another string.
When we call ss[6:11],
we are calling the substring Shark that exists within the string Sammy Shark!."""
