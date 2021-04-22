def diStringMatch(s):
    """
    string = "IDID"
    permutation of intigers [0, n] included in string , of length n

    len(string) = 4
    permutation of numbers [0, 1, 2, 3, 4]

    if
    perm[i] < perm[i+1] ==> I
    perm[i] > perm[i+1] ==> D

    "IDID":

    where I - > put minimum
    where D -> put max

    """
    numbers = []
    length_of_string = len(s)
    for el in range(0, length_of_string + 1, 1):
        numbers.append(el)

    result = []

    for el in s:
        if el == "I":
            #current_minimum =
            result.append(numbers.pop(0))
        if el == "D":
            result.append(numbers.pop())

    result.append(numbers.pop())

    return result

if __name__ == "__main__":
    print(diStringMatch("IDID"))