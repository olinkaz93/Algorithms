class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

#if we need to implement queue using the stack,
#we are able use the push() and pop () methods from the stack
#so we can only put push() - add the element to the end of implemented array
#and pop() - which removes the last element from the implemented array
#however for queues , we must to to DEQUEUE elements (which is removing the FIRST element)
#so to be able POP (dequeue) the first element from the queue, we must move them in reversed order to the other stack
#we will use two stacks
"""
Possible scenario:

to enqueue - push () elements to the first stack1 (S1):

4       last element 
3    
2       second element
1       first element
S1  S2

to dequeue - (if the S2 is empty) - we must pop () elements from the stack 1 -> and then push () them to the stack 2
having that made, we will have the elements in the reversed order (upside down in S2 then before the action in S1)
Then we can POP () the  last element from the Stack 2:

     1    last element
     2
     3    second element
     4    first element
S1  S2  

then we can pop() - the LAST element / from the Stack2

     x   we remove the (1) which was the last element in S2 before
     2
     3
     4 
S1  S2  

if we want to continue dequeue and pop() the elements from the queue, the elements are awaiting is S2, so if we want to
dequeue the element, we must to pop () the (last) element from the S2

     x   
     x  we remove the (2) which was the last element in S2 before
     3
     4 
S1  S2  

to enqueue - add more elements (5,6) to our queue we can push () them to the S1

          last element
     
6    3    second element
5    4    first element
S1  S2  

then, if we dequeue if our stack 2 has elements we must remember that those elements are first to delete
we stil pop() elements from the S2 as they keep the QUEUE ordered elements 

          last element
     
6    x    second element
5    x    first element
S1  S2  

if we want to keep on removing, and S2 is empty, we must first pop() elements from the S1 and push() them into S2

          last element
     
     5    second element
     6    first element
S1  S2  

"""

class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    #we add the elements only to the first stack - S1
    def enqueue(self, data):
        new_element = Node(data)
        self.stack1.append(new_element)
        #print("length stack1: ", len(self.stack1))

    #when we dequeue - we must (1) - pop () elements from the S2 - if nothing is there, we must first pop() elements
    #from the S1 -> S2, push them there, and then pop() element from the Stack2

    def dequeue(self):
        #when we have only one element is S1, and no elements in S2, we can only pop() element from the S1
        if (len(self.stack1) == 0 and len(self.stack2) == 0):
            print ("no elements to delete, empty queue!")
        elif (len(self.stack1) == 1 and len(self.stack2) == 0):
            self.stack1.pop()
        else:
            #otherwise if there are elements in the S1 and  NO elements in S2
            #we must reverse the order of elements in S1 and put them in S2 - via pop () from S1 and push() into S1,
            #then we can pop () element from the S2
            if (len(self.stack1) and len(self.stack2) == 0 ):

                #we pop() whole elements from S1 to S2
                while (len(self.stack1) > 0):
                    last_element_in_s1 = self.stack1.pop()
                    self.stack2.append(last_element_in_s1)
                #then we pop() the very last element from S2
                self.stack2.pop()

            elif (len(self.stack2) > 0):
                self.stack2.pop()



    def print_elements(self):
        # to print elements, we must first to print the elements which are in S2, and then again push() all elements
        # from the S1 to S2, and then continue printing the elements
        if (len(self.stack1) == 0 and len(self.stack2) == 0):
            print("The queue is empty! Nothing to print")

        else:
            if (len(self.stack2) > 0):
                for el in range(len(self.stack2) - 1, -1, -1):
                    print(self.stack2[el].data)

            for el in range(0, len(self.stack1), 1):
                print(self.stack1[el].data)



if __name__ == "__main__":

    queue_made_with_stack = Queue()
    print(type(queue_made_with_stack))
    queue_made_with_stack.enqueue("1 hello!!!")
    queue_made_with_stack.enqueue("2 hi!!!")
    queue_made_with_stack.enqueue("3 hola!!!")
    queue_made_with_stack.enqueue("4 ahoy!!!")


    queue_made_with_stack.print_elements()

    queue_made_with_stack.dequeue()
    queue_made_with_stack.print_elements()
    queue_made_with_stack.dequeue()
    queue_made_with_stack.print_elements()
    queue_made_with_stack.enqueue("5 bye bye!!")
    queue_made_with_stack.print_elements()
    queue_made_with_stack.dequeue()
    queue_made_with_stack.print_elements()
    queue_made_with_stack.dequeue()
    queue_made_with_stack.dequeue()
    queue_made_with_stack.print_elements()
    queue_made_with_stack.dequeue()
    queue_made_with_stack.print_elements()
    queue_made_with_stack.print_elements()
    queue_made_with_stack.enqueue("new round!")
    queue_made_with_stack.print_elements()
    queue_made_with_stack.dequeue()
    queue_made_with_stack.print_elements()
    #print(len(queue_made_with_stack.stack1))
    queue_made_with_stack.print_elements()
    queue_made_with_stack.print_elements()
    print("queue: 1, 2, 3")
    queue_made_with_stack.enqueue("1")
    queue_made_with_stack.enqueue("2")
    queue_made_with_stack.enqueue("3")
    queue_made_with_stack.print_elements()
    print("queue: 2, 3")
    queue_made_with_stack.dequeue()
    queue_made_with_stack.print_elements()
    print("queue: 2, 3, 4")
    queue_made_with_stack.enqueue("4")
    queue_made_with_stack.print_elements()
    queue_made_with_stack.dequeue()
    print("queue: 3, 4")
    queue_made_with_stack.print_elements()
    queue_made_with_stack.dequeue()
    queue_made_with_stack.dequeue()
    print(len(queue_made_with_stack.stack1))
    print(len(queue_made_with_stack.stack2))
    queue_made_with_stack.dequeue()
    queue_made_with_stack.print_elements()











