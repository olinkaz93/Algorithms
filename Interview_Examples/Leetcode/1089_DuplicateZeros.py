"""
1089. Duplicate Zeros

Given a fixed length array arr of integers,
duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

 Example 1:
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]

https://www.youtube.com/watch?v=io3N5YTFbxM

"""


def duplicateZeros(arr):

    for i in range(0, len(arr), 1):
        if arr[i] != 0:
            arr[i] = arr[i]
        else:
            arr[i] = 0
            next_index = i+1
            while(next_index < len(arr)):
                


if __name__ == "__main__":
    print(duplicateZeros([1,0,2,3,0,4,5,0]))
    #[1,0,0,2,3,0,0,4]
