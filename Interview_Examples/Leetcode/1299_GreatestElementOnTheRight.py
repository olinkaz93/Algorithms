"""
1299. Replace Elements with Greatest Element on Right Side
Given an array arr,
replace every element in that array
with the greatest element among
the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation:
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
"""



def replaceElements(arr):
    # if array has only one element, we return [-1]
    if len(arr) == 1:
        return [-1]

    # for more elements we loop at ech of them,
    # assign the max element on the right "max(arr[index + 1:])"
    # and the last we assign the last element as -1

    else:
        for index in range(0, len(arr) - 1, 1):
            arr[index] = max(arr[index + 1:])

            # assign the last element
        arr[len(arr) - 1] = -1
    return arr


if __name__ == "__main__":
    result = replaceElements([9,0,4,2,22,0,4,9])
    print(result)