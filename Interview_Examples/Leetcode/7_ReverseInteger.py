def reverseInt(x):
    number = str(x)
    #print(x)

    reversed_number = ""

    # if(str[0] == "-"):
    #    reversed_number += "-"

    right_pointer = len(number) - 1

    while (number[right_pointer] != 0 and right_pointer >= 0):
        right_pointer -= 1
        print("pointer", right_pointer, " ", number[right_pointer])

    for right_pointer in range()



if __name__ == "__main__":
    reverseInt(-190)