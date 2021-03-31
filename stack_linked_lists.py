class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

#implementation of the stack with the Linked List
#the Stack is FIFO, high-level data structure, that might be implemented with Arrays(list - in Python) and/or Liked/List
#implememting the class Stack
"""
-                   - Amazon  
-         - Uber    - Uber    - Uber
- Google  - Google  - Google  - Google  - Google _______ 
"""
class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    #push method to insert the node(data) on the TOP of the STACK, think about the plate over the plate
    #the first inserted item will go to the bottom of the STACK

    def push(self, data):
        new_node = Node(data)
        #if we add the very first item we need to put it on the very bottom of the stack, so it will be BOTTOM and TOP
        #item at the same time

        if self.length == 0:
            self.top = new_node
            new_node.next = self.bottom
            self.bottom = self.top
            self.length += 1

        else:
            new_node.next = self.top
            self.top = new_node
            self.length += 1

    #push method to remove the very top element from the stack, if there is only one element of the stack,
    #we must also clear the very bottom of the stack

    def pop(self):
        if self.length == 0:
            print("Nothing to remove, empty stack")
        elif self.length == 1:
            self.top = None
            self.bottom = None
            self.length -= 1
        else:
            second_top = self.top.next
            self.top = second_top
            self.length -= 1

    #peek method just to check the top value of the stack
    def peek(self):
        if self.length == 0:
            print ("empty stack")
            return None
        else:
            return self.top.data

    def print_stack(self):
        if self.length == 0:
            print("nothing to print!")
        else:
            element_to_print = self.top
            while (element_to_print != None):
                print(element_to_print.data)
                element_to_print = element_to_print.next

if __name__ == '__main__':

    my_stack = Stack()
    my_stack.push("Google")
    my_stack.push("Uber")
    my_stack.push("Amazon")



    my_stack.print_stack()
    print("TOP", my_stack.top.data)


    print("BOTTOM", my_stack.bottom.data)



