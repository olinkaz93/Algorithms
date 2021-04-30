"""
394. Decode String
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].


Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""


def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    """
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"

    We can loop through the string
    and once we see a digit number "chunk" of string
    will be "number*" than if we see "[" we increment counter
    than when wee see char we add it to the "number * ( char)"
    if we see "]" we countdown, if count = 0, we close the chunking and add +

    """

    """
    "3[a]2[bc]"
    +3 *(a) + 2*(bc) 
    """

    result = []
    chunk = []
    counter = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for el in s:
        if el.isdigit():
            print(el)
            chunk.append(int(el))
        elif el == "[":
            # chunk.append(el)
            counter += 1
        elif el in alphabet and counter == 0:
            result += str(el)
        elif el in alphabet and counter != 0:
            # print("letter!", str(el))
            chunk.append(str(el))
        elif el == "]":
            counter -= 1
            # chunk.append(el)
            if counter == 0:
                #print(type(chunk))
                # result.append(chunk)
                elements = chunk[0]
                while (elements > 0):
                    for i in range(1, len(chunk), 1):
                        result.append(chunk[i])
                    elements -= 1
                chunk = []
        #print(type(result))
    print("result!", result)
    for el in result:
        print(el)

        #decoded = "".join(result)
        #print(decoded)
        #return result

if __name__ == "__main__":
    decodeString("2[abc]3[cd]ef")