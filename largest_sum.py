#Have the function LongestWord(sen) take the sen parameter being passed
# and return the largest word in the string.
# If there are two or more words that are the same length,
# return the first word from the string with that length.
#Ignore punctuation and assume sen will not be empty.


#having the input as a string we can create a list with each separate word (that would make an extra space allocation
#we can loop over the list of those words and then update the lenght os the MAXimum length of the word
#ignore punctuation

#when we loop over the each word then we need to check also wethear there is no punctuation, so it would create nested loop,
#that should be avoided

#better to loop thorugh the sentence, which is already a list itself and and we check every character
#not counting punctuation and treating spacebar as the separation

#>>> mylist = ['123','123456','1234']
#>>> print max(mylist, key=len)
#123456

def LongestWord(sen):

    maximum_length = 0
    current_max_length = 0
    current_word = ""

    for char in sen:

        if char 










  return words

# keep this function call here
print(LongestWord(input("Give me the sentence")))