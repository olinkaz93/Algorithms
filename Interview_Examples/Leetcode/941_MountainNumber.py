"""
Given an array of integers arr,
return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
https://www.youtube.com/watch?v=-gL730m25v8
https://www.youtube.com/watch?v=kSB6neKxIME 
"""

def validMountainArray(arr):
    left_pointer = 0
    right_pointer = len(arr) - 1

    if (len(arr)) == 1:
        return False
    if (len(arr)) == 2:
        return False

    while (left_pointer < right_pointer):

        print("left pointer ", left_pointer, " right ", right_pointer)
        if arr[left_pointer] < arr[left_pointer + 1]:
            left_pointer = left_pointer + 1
        if arr[right_pointer - 1] > arr[right_pointer]:
            right_pointer = right_pointer - 1
        else:
            break

    if left_pointer == right_pointer and left_pointer!=0 and right_pointer != len(arr) - 1:
        return True
    else:
        return False



if __name__ == "__main__":

    array = [9,8,7,6,5,4,3,2,1,0]
    result = validMountainArray(array)
    print(result)
