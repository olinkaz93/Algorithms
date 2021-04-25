"""
You're given strings jewels representing
the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive,
so "a" is considered a different type of stone from "A".

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0

"""


def numJewelsInStones(jewels, stones):


    dict_stones = {}
    result = 0

    for stone in stones:
        if stone not in dict_stones:
            dict_stones[stone] = 1
        else:
            dict_stones[stone] += 1

    for key in dict_stones.keys():
        if key in jewels:
            result += dict_stones[key]

    return result

if __name__ == "__main__":
    jewels = "z"
    stones = "ZZ"
    print(numJewelsInStones(jewels, stones))