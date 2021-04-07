#Write a program that console logs the numbers from 1 to n
#but for the multiple of three print "fizz"
#instead of the number and for the multiples
#of five print "buzz"
#For numbers which are multiples of both three and five print "fizzbuzz"

#example:
# fizzBuzz(5):
# 1
# 2
# fizz
# 4
# buzz

"""
for this kind of task, we ust use "modulo"
% and determin whether the number can be divide or not
"""

def fizzBuzz(n):

    for i in range(0, n, 1):
        output = i+1
        #print(output)

        if (output % 3 == 0 and output % 5 == 0 ):
            print(output, "fizzbuzz")
        elif (output % 3 == 0 and output % 5 != 0):
            print(output, "fizz")
        elif (output % 3 != 0 and output & 5 == 0):
            print(output, "buzz")
        else:
            print(output)





if __name__ == "__main__":

    number = 35
    fizzBuzz(number)