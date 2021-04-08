# [1, 9]
# [2, 0]

""" if we have 9 , we must add +1 , update the value for : 0 and, add the "1" to the previous index, while it is not !=9 or
if exceeds, we create one more variable, at the beginning of the array, and extend the array
"""

def addOne(digits):

    #if the last element is less than 9, we add +1 and return the digits
    if digits[-1] < 9:
        digits[-1] = digits[-1] + 1
        return digits
    #otherwise if the digit is = 9, we must assign it as 0, and add 1 to the next element in the array, which will be less then 9
    #if we would loop over the array, we must assign all numbers as 0 and add 1, to the beginning of the array
    elif len(digits) == 1 and digits[0] == 9:
        return [1, 0]

    elif digits[-1] == 9:
        digits[-1] = 0
        index = -2
        #print(index, "value", digits[index])
        #print(digits[-(len(digits))])
        while index >= -(len(digits)):
            if digits[index] < 9:
                digits[index] = digits[index] + 1
                return digits
            elif digits[index] == 9 and index != -(len(digits)):
                digits[index] = 0
                index = index - 1
                #print("i am at: ", index)
            elif digits[index] == 9 and index == -(len(digits)):
                digits[0] = 0
                digits.insert(0, 1)
                return digits

if __name__ == "__main__":

    digits = [9, 9, 9]
    result = addOne(digits)
    print(result)
