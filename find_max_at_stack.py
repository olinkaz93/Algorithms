"""
Use your Stack class to implement a new class MaxStack
with a method get_max() that returns the largest element
in the stack. get_max() should not remove the item.
Your stacks will contain only integers.
"""

"""
Stack   Stack_max


20      20

===================
Stack   Stack_max

1
20      20

===================

Stack   Stack_max

200
1	    200
20      20

===================

Stack   Stack_max

200
1	    200
20      20

===================

Stack   Stack_max

2
200
1	    200
20      20

===================
"""
#whenever there is value bigger then current_max, we pu the max on max_stack, so we can store all maxes in them
#when we pop() elements  and if we encoutner the current max of the stack we must pop() the element from both stacks


class Stack():

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


class MaxStack():
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, item):
        """if the length of the stack is == 0 , then we also must push()/append this item onto max_stack """
        if (len(self.stack.items) == 0):
            self.stack.push(item)
            self.max_stack.push(item)
            #if we have already one element in our stack we must check whether the element is not bigger than current
            #element on top on the max_stack, if it is , we will add it there also
        else:
            self.stack.push(item)
            if (item > self.max_stack.peek()):
                self.max_stack.push(item)

    def pop(self):
            #when we remove the element form the stack, we need to also check whether is not the MAX at this moment,
            #if it is current_max we must remove this element also from the TOP of the MAX_STACK
            if (len(self.stack.items)) == 0:
                print("nothing to remove, empty stack!")
            #if it is only one element in the stack, we must to remove the item from both STACK and MAX_STACK
            elif (len(self.stack.items)) == 1:
                self.stack.pop()
                self.max_stack.pop()
            else:
                removed_element = self.stack.pop()
                if removed_element == self.max_stack.peek():
                    self.max_stack.pop()

    def max_element(self):
        if len(self.max_stack.items) == 0:
            print("nothing to print, we have no elements in stack")
            return None
        else:
            max_element = self.max_stack.peek()
            return max_element

    def print_stack(self):
        for i in range(0, len(self.stack.items), 1):
            print("item", i, " ", self.stack.items[i])

    def print_max_stack(self):
        for i in range(len(self.max_stack.items)-1, -1, -1):
            print("max_stack item", i, " ", self.max_stack.items[i])

if __name__ == "__main__":

    new_stack = MaxStack()
    new_stack.push(1)
    new_stack.print_stack()
    new_stack.push(2)
    new_stack.push(3)
    new_stack.push(4)
    new_stack.push(5)
    print("MY STACK")
    new_stack.print_stack()
    print("MAX STACK")
    new_stack.print_max_stack()
    new_stack.push(0)
    new_stack.push(10)
    print("MY STACK")
    new_stack.print_stack()
    print("MAX STACK")
    new_stack.print_max_stack()

    max_element = new_stack.max_element()
    print("the max element is: ", max_element)

    new_stack.push(20)
    max_element = new_stack.max_element()
    print("the max element is: ", max_element)

    new_stack.pop()
    print("MY STACK")
    new_stack.print_stack()
    print("MAX STACK")
    new_stack.print_max_stack()
    max_element = new_stack.max_element()
    print("the max element is: ", max_element)
    new_stack.push(1000000000000)
    print("MY STACK")
    new_stack.print_stack()
    max_element = new_stack.max_element()
    print("the max element is: ", max_element)
    new_stack.push(88)
    new_stack.print_stack()
    max_element = new_stack.max_element()
    print("the max element is: ", max_element)
    print("MAX STACK")
    new_stack.print_max_stack()


