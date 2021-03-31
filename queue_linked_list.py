#implementation of queue using linked_list
#it is a better approach to implement it with linked list than arrays (list)
#when we want to enqueue or dequeue element we simply get the first/last element, and no need to shift all elements
#like it must have happened at the lists

#lets create a Class node

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    #when adding the elements to the queue, we add them to the end of the queue
    #one, by one and linking them
    def enqueue(self, data):
        new_node = Node(data)
        #when is the first element in the queue we must point the first element as a new node
        #and point it also as the last element
        if (self.length == 0):
            self.first = new_node
            self.last = new_node
            self.length += 1
        else:
        #when we have more elements then only one we must link the last element to our new_node
        #and assign the new_node as the new LAST element
            self.last.next = new_node
            self.last = new_node
            self.length += 1


    def dequeue(self):
        #removing the element from the queue, is removing the very first element
        #our edge cases are
        #when there is no element in the queue
        if (self.length == 0):
            print("nothing to remove! empty queue")
        #when there is only one element in the queue
        elif (self.length == 1):
            self.first = None
            self.last = None
            self.length = self.length - 1
        # in other cases to remove the element we need to access the very first element from our queue end remove it
        # before that we must find the successor of the first element, so that element will be our new FIRST element
        else:
            second = self.first.next
            self.first = second
            self.length = self.length - 1

    #peek method is to show the very first element in the queue
    def peek(self):
        if self.length == 0:
            print("no elements to show, the queue is empty")
            return None
        else:
            first_element_in_the_queue = self.first
            print("very first item", first_element_in_the_queue.data)


    def print_values(self):
        if (self.length == 0):
            print("nothing to pring, empty QUEUE")
        else:
            element_to_print = self.first
            while (element_to_print != None):
                print(element_to_print.data)
                element_to_print = element_to_print.next



if __name__ == "__main__":

    new_queue = Queue()
    new_queue.enqueue("Hello")
    print("my first element", new_queue.first.data)
    new_queue.enqueue("Hi")
    print("my last element", new_queue.last.data)
    new_queue.enqueue("hakuna!")
    print("my last element", new_queue.last.data)
    new_queue.enqueue("BLA BLA BLA")
    print("my last element", new_queue.last.data)
    new_queue.print_values()
    print("removing elemnts!")
    new_queue.dequeue()
    print("my first element", new_queue.first.data)
    new_queue.print_values()
    new_queue.peek()


