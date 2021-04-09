#the problem is to remove the duplicate number from the sroted array, but we cannot change it.
#the key for algorithm is to track the SLOW runner_pointer, that will indicate an index of current elements unrepeated
#in the list and than fast RUNNER index, thay will loop thorugh all the list, and once, it is different value, we will
#assign a pointer of index +1, and coinitnue looping

#https://www.youtube.com/watch?v=nRKZC2JF7LU

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numbers = nums
        current_number = 0
        # next_unique_number = current_number + 1

        # [1,2,3,4,4]
        # [1,1,2,2,3]
        # [1,2,3,3,3]
        # number[current_number] - is always unique
        for next_unique_number in range(1, len(numbers), 1):
            if numbers[next_unique_number] != numbers[current_number]:
                current_number += 1
                numbers[current_number] = numbers[next_unique_number]

        return current_number + 1





