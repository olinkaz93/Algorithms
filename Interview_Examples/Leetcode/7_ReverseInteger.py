"""
7. Reverse Integer

Given a signed 32-bit integer x,
return x with its digits reversed.
If reversing x causes the
value to go outside the
signed 32-bit integer range [-231, 231 - 1],
then return 0.

Assume the environment
does not allow you to
store 64-bit integers
(signed or unsigned).
https://www.youtube.com/watch?v=CRgXG1vK-wg
"""

def reverseInt(x):
    reversed = 0
    sign = -1 if x < 0 else 1
    x = abs(x)

    while x > 0:
        #pop - always last intiger
        pop = x % 10
        #we shorten the intiger 123 // 10 = 12
        x //= 10
        #multiply * 10 so we make extra space for 'pop' element
        reversed = reversed * 10 + pop

    if reversed > -2 ** 31 and reversed < 2 ** 31 - 1:
        return reversed * sign

    return 0

if __name__ == "__main__":
    print(reverseInt(-190))