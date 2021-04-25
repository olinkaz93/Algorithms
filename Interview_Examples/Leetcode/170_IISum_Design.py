"""
Design a data structure that accepts a stream of integers
and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:
TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.

Example 1:
Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]

Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false

"""

class TwoSum():

    def __init__(self):
        self.list = []

    def add(self, number):

        self.list.append(number)

    def find(self, value):
        """
       Find if there exists any pair of numbers which sum is equal to the value.
        """
        if len(self.list) == 0 or len(self.list) == 1:
            return False

        #if len(self.list) == 2 and self.list[0]+self.list[1] == value:
        #    return True

        self.list.sort()
        print(self.list)
        left_pointer = 0
        right_pointer = len(self.list)-1

        while (left_pointer < right_pointer):
            if self.list[left_pointer] + self.list[right_pointer] == value:
                return True
            if self.list[left_pointer] + self.list[right_pointer] > value:
                right_pointer -= 1
            if self.list[left_pointer] + self.list[right_pointer] < value:
                left_pointer += 1

        return False



if __name__ == "__main__":

    mySum = TwoSum()
    mySum.add(1)
    print(mySum.list)
    mySum.add(3)
    print(mySum.list)
    mySum.add(5)
    #print(mySum.list)
    #mySum.find()
    #print(mySum.list)
    result = mySum.find(4)
    print(result)
    result = mySum.find(7)
    print(result)