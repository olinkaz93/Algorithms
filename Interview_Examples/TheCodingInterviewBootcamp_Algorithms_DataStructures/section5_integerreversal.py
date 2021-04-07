#Given an integer,
#return an integer that is the reverse
#ordering of numbers
# -- Examples
# reverseInt(15) === 51
# reverseInt(-15) === -51
# reverseInt(-90) === -9
# reverseInt(981) === 189
# reverseInt(500) === 5

def reverse_int(number):
    string_number = str(number)
    #print(type(string_number))

    reversed_number = ""
    #print(type(string_number[0]))
    #if string_number[0] == "-":
    #    reversed_number = "-" + reversed_number

    if len(string_number) == 1 and string_number[0] == "0":
        result = 0
        return result


    for index_in_string_number in range (len(string_number)-1, -1, -1):
        #when there is no element in our reversed number, we cannot add "0" from the input number
        #so we continue, until we find very first element !- "0" which will fill the reversed_number
        if string_number[index_in_string_number] == "0" and reversed_number == "":
            continue
        if index_in_string_number == 0 and string_number[index_in_string_number] == "-":
            reversed_number = string_number[index_in_string_number] + reversed_number
        else:
        #print(string_number[index_in_string_number])
            reversed_number = reversed_number + string_number[index_in_string_number]

    #print(reversed_number)
    result = int(reversed_number)
    return result



if __name__ == "__main__":
    number = 0
    result = reverse_int(number)
    print("before", number)
    print("after", result)
    print(type(result))

    """
    We could have used also reverse function on the string number, and then parse it again to int.
    That would automatically remove the leading 'zeros',
    and for he negative '-' we can check if input < 0, then we multiply result * (-1) 
    print("========================")
    result = reverse(string_number)
    print(type(result))
    print(result)
    result=int(result)
    print(result)
    
    """