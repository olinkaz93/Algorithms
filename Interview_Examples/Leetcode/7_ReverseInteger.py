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

    #for pointer in range(right_pointer, -1, -1):
    #    reversed_number += number[pointer]
    #    if pointer == 0 and number[pointer] == "-1":
    #        return -(int(reversed_number))
    #    else:
    #        return int(reversed_number)

if __name__ == "__main__":
    reverseInt(-190)