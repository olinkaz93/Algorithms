def reverseString(word):

    input = list(word)

    left_index = 0
    right_index = len(input)-1

    # hello
    # oellh
    # olleh
    result=[]
    for i in range (0, len(input), 1):
        result.append(input.pop())

    reversedWord = ''.join(result)
    print(reversedWord)

def reverse(word):

    inputWord = word[::-1]
    for el in inputWord:
        print(el)

    print(inputWord)


if __name__ == "__main__":
    reverseString("hello")

    reverse("hey")
