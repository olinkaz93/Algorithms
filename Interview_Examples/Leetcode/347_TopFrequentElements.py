"""
347. Top K Frequent Elements
Medium

Given an integer array nums and an integer k,
return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

"""

def topKFrequent(nums, k):
    # 1) Create the dictionary of the elements in nums, num -> frequency

    # 2) Create the bucket with the length of nums+1, where each index -> frequency of the element

    # 3) iterate from the back of the bucket until you reach upmost k elements
    dictionary_nums = {}
    bucket = [None]
    # nums = [1,1,1,2,2,3]
    result = []
    for num in nums:
        bucket.append(None)
        if num not in dictionary_nums:
            dictionary_nums[num] = 1
        else:
            dictionary_nums[num] += 1
    # we create bucket that index coresponds to the frequency (value) of certain key, so we put
    for key, value in dictionary_nums.items():
        if bucket[value] == None:
            bucket[value] = [key]
        else:
            bucket[value].append(key)
        # print(bucket[value])
    # print(bucket)

    for i in range(len(bucket) - 1, -1, -1):
        if bucket[i] != None and len(result) < k:
            for el in bucket[i]:
                result.append(el)

    return result



if __name__ == "__main__":
    nums = [1]
    k = 1
    result = topKFrequent(nums, k)
    print(result)
