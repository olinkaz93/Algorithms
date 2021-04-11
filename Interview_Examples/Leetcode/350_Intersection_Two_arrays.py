"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]


nums1 = [1,1,2,2]
nums2 = [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.


nums1 = [4,5,9]
nums2 = [4,4,8,9,9]

https://www.youtube.com/watch?v=lKuK69-hMcc
"""

def findIntersection(list1, list2):

    if(len(list1) >= len(list2)):
        first_list = list1
        second_list = list2
    else:
        first_list = list2
        second_list = list1

    numbers_first_list_dictionary = {}
    #we create a hash map of our first list, which will store the number, as a key, and the occurency as a value
    for number in first_list:
        if number not in numbers_first_list_dictionary:
            numbers_first_list_dictionary[number] = 1
        else:
            numbers_first_list_dictionary[number] += 1

    print(numbers_first_list_dictionary)

    #having the list, we can loop over the second list, and compare if value, exists
    #if it so, we will add the common number to the result, and decrement the value of the occurent number in list1
    result = []

    for number in second_list:
        if number in numbers_first_list_dictionary and numbers_first_list_dictionary[number] > 0:
            result.append(number)
            numbers_first_list_dictionary[number] -= 1

    print(result)





if __name__ == "__main__":
    list_a = [1,2]
    list_b = [1,1]

    findIntersection(list_a, list_b)
