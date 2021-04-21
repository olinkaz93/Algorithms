"""
Implement strStr().

Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string?
This is a great question to ask during an interview.

For the purpose of this problem,
we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().
https://www.youtube.com/watch?v=BXCEFAzhxGY
"""

def strStr(haystack, needle):
    """
    if len(needle) > len(haystack):
        return 0

    left_pointer = 0
    right_pointer = len(needle)

    #print(right_pointer)

    #while(right_pointer < len(haystack)):

   # for left_pointer in range(0, len(haystack)-len(needle)-1, 1):
    #    print("left pointer", left_pointer)
    #    right_pointer = left_pointer + len(needle) - 1
    #    print("right pointer", right_pointer)
        #if (haystack[left_pointer] == needle[left_pointer])
    while (left_pointer < right_pointer and right_pointer < len(haystack)-1):
        print(haystack[left_pointer])
        print(haystack[left_pointer])
        left_pointer += 1
        right_pointer += 1
        if(haystack[left_pointer] == needle[left_pointer]):
            print("same")

            https://www.youtube.com/watch?v=JG2VSsgYWuo



            # solution https://www.youtube.com/watch?v=RDYZCErOQws&t=277s
    """

    for i in range(len(haystack) - len(needle) + 1):
        # In this way, you create many objects of substrings, which makes space complexity NOT O(1) !

        #if haystack[i:i + len(needle)] == needle:
        #    return i
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
            if j == len(needle) - 1:
                return i
    return -1



if __name__ == "__main__":
    print(strStr("string", "ri"))


