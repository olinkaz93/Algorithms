"""
Given an integer array nums,
return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate
triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""

#we can sort the list, so that will save out time complexity
#sorting is big O(n log n)
#and once having the start_element, we set the pointers
#if current sum is lower than target sum, we will increment the index
#if current sum is lower then target sum, we will go to the next one
#we can make a while loop, until left_index < right_index

#https://www.youtube.com/watch?v=hNRS81I1OZ8

def threeSum(list_of_numbers):

    if len(list_of_numbers) < 3:
        return ([])

    triplets = []

    #starting with sorting
    list_of_numbers = sorted(list_of_numbers)
    print(list_of_numbers)

    for index in range(0, len(list_of_numbers)-2, 1):

        #edge cases
        if list_of_numbers[index] > 0:
            break

        if list_of_numbers[index] == list_of_numbers[index-1] and index > 0:
            continue

        lower_index = index + 1
        upper_index = len(list_of_numbers) - 1

        while lower_index < upper_index:

            sum = list_of_numbers[index] + list_of_numbers[lower_index] + list_of_numbers[upper_index]
            if sum == 0:
                triplets.append([list_of_numbers[index], list_of_numbers[lower_index], list_of_numbers[upper_index]])
                #lower_index = lower_index + 1
            if sum <= 0:
                lower_index = lower_index + 1
                while(list_of_numbers[lower_index] == list_of_numbers[lower_index-1] and lower_index < upper_index):
                    lower_index = lower_index + 1
            else:
                upper_index = upper_index - 1

    return (triplets)

if __name__ == "__main__":

    print(threeSum([9, -9, 0, 3, 0, -3, 3, 0]))

