#given an an array, tell me the first recurring element

#given array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
#should return 2

#givven array = [2, 1, 1, 2, 3, 5, 1, 2, 4]
#should give 1

#given array = [2, 3, 4, 5
#should give Null

#so can we assume that array has only intigers?
#we should also return Null when there is:
#-no reacurring elemenet
#-when list is empty

#we can create a dictionary, dict.key = value, where
#key = index of element
#value = value of the element
#if there are two values of the same, we must check indexes
#so we find first reoccurence, when the 2nd element will be at
#index lower than another one

#we can create a dictionary, where the key will be a value
#and value will be a list of indexes

#e.g. list = [2, 1, 1, 2, 3, 5, 1, 2, 4]

def reocurrence(list_of_numbers):

    if(list_of_numbers == []):

        return None

    dictionary_of_numbers = {}
    length = len(list_of_numbers)

    for index_number in range(len(list_of_numbers)):
        #index = 0
        current_number = list_of_numbers[index_number]
        #checking the numbers which appears exactly twice
        if (list_of_numbers.count(current_number)) == 2:
            print("the element", current_number, " al ready exists")
            print (list_of_numbers[index_number], " at index", index_number, " exits more than 2")
            print("########################")
            #dictionary's keys must be unique, so if there is no such a value we create anew key with the value - index of the number
            if (dictionary_of_numbers.get(current_number) == None):
                dictionary_of_numbers[current_number] = [index_number]
                print(dictionary_of_numbers)
            #otherwise, if the double number appears already in the diciotnary, we add the 2nd index of the number
            else:
                current_indexes = dictionary_of_numbers.get(current_number)
                print("current indexes of", current_number, ":", current_indexes)
                dictionary_of_numbers[current_number] = current_indexes + [index_number]

    #printing the dictionary of numbers which values are double
    print(dictionary_of_numbers)

    #we make a list where we will access the lowest number of the second value
    second_reocurrence = []
    for key in dictionary_of_numbers:
        second_reocurrence.append(dictionary_of_numbers[key][1])

    print(second_reocurrence)
    value_of_second_minimal_reocurrence = min(second_reocurrence)
    print(value_of_second_minimal_reocurrence)

    # 2) other idea is just to find the minimum directly at the dictionary
    for key in dictionary_of_numbers:
        print(dictionary_of_numbers[key][1])
    print("minimum second")

    first_reoccuring_number = list_of_numbers[value_of_second_minimal_reocurrence]
    return first_reoccuring_number

sample_list = [1,2, 4, 4, 0, 2, 4, 5, 5]
result = reocurrence(sample_list)
print("The first reoccuring number is", result)


