"""
622. Design Circular Queue

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.


Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4


Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
"""

"""
The queue module defines the following classes and exceptions:

class queue.Queue(maxsize=0)
Constructor for a FIFO queue. maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will block once this size has been reached, until queue items are consumed. If maxsize is less than or equal to zero, the queue size is infinite.
"""
"""
from queue import Queue


def circularQueue():

    my_queue = Queue(2)
    my_queue.put("hello")
    my_queue.put("hi")
    print(my_queue.qsize())
    print(type(my_queue))
    print(my_queue)
    print(my_queue.get())
    print(my_queue.qsize())
    """


class MyCircularQueue:

    def __init__(self, k):
        """
        :type k: int
        """
        self.list = [-1]*k
        self.size = 0
        self.front = 0
        self.end = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if (self.size == 0):
            self.list[self.front] = value
            self.size +=1
        elif (self.isFull()):
            print("Full Queue! Cannot add more!")
            return False
        else:
            self.end += 1
            self.size += 1
            self.end = self.end % len(self.list)
            self.list[self.end] = value


    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            print("Empty Cirular Queue!")
            return False
        else:
            value = self.list[self.front]
            self.size -= 1
            self.front += 1
            self.front = self.front % len(self.list)
            # [ -1, -1, -1, -1, X]
            # if I remove X, that is index 4, length of QueueList is 5, so if I increment front index + 1,
            # we must reassign as  0 => 5 mod 5 => 0 , so we will be ae at the beginning of the list
            return value

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            print("Empty Circular Queue!")
            return None
        else:
            return self.list[self.front]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            print("Empty Circular Queue!")
            return None
        else:
            return self.list[self.end]

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self):
        """
        :rtype: bool
        """
        if self.size == len(self.list):
            return True
        else:
            return False

if __name__ == "__main__":

    circular = MyCircularQueue(5)
    print(circular)
    print(circular.isFull())
    print(circular.isEmpty())
    print(circular)
    print(circular.Front())
    print(circular.Rear())
    circular.enQueue(50)
    circular.enQueue(1)
    circular.enQueue(2)
    circular.enQueue(3)
    circular.enQueue(40)
    circular.enQueue(100)

    print(circular.Front())
    print(circular.deQueue())
    print(circular.deQueue())
    print(circular.deQueue())
    print(circular.deQueue())
    print(circular.deQueue())
    print(circular.deQueue())


