#We define a class Stack with the array which will store the elements and the methods we require for a stack
class Stack():

#The constructor consists of only an empty array as length comes built-in with arrays(lists)
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)

    def pop(self):
        self.array.pop()

    def print(self):
        #order of inserted values
        #for i in range(len(self.array)):
        #    print(self.array[i])
        #reversed order from back to the front
        for i in range(len(self.array) -1, -1 ,-1):
            print("index", i, " ", self.array[i])


if __name__ == '__main__':

    my_stack = Stack()
    my_stack.push("google")
    my_stack.push("uber")
    my_stack.push("amazon")
    my_stack.print()