"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
https://www.youtube.com/watch?v=qq64FrA2UXQ

"""

"""
Example 1: Convert integer to binary using bin()
number = 5

print('The binary equivalent of 5 is:', bin(number))
Output
The binary equivalent of 5 is: 0b101
The prefix 0b represents that the result is a binary string."""

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    # we convert the string to int, base 2

    "0011"
    "0010"

    """
    1) making "addition" with XOR operation ^
    
 a  0011
 b  0010
    ____
 s  0001  < === we keep it as new A , to which we add b + carry in next step
    
    2) adding: bit operation & (logical AND)
    
 a  0011
 b  0010
    ____
 c  0010   < === we keep it as the 'carry'
    
    3) we shift << shifted carry - from step 1 (c 0010):
    
    0010 << 0100
    
    4) (1) we add (sum/ from the first iteration + shifted carry, and so on), until carry is empty:
    
        && operation 
        
 s  0001 
 c  0100 
    ____
    0101   ==== > result 0110 (5 decimal)
      
    5) 
    """


    x = int(a, 2)
    y = int(b, 2)
    print(x, y)
    while (y != 0):
        answer = x ^ y
        carry = (x & y) << 1
        x = answer
        y = carry

    binary_string = bin(x)[2:]
    #print(type(x))
    return binary_string

if __name__ == "__main__":

    result = addBinary("0011", "0010")
    print(result)

