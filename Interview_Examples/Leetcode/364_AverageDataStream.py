"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.


Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3


Constraints:

1 <= size <= 1000
-105 <= val <= 105
At most 104 calls will be made to next.
"""
"""
from queue import Queue


class MovingAverage():

    def __init__(self, size):
        self.size = size
        self.queue = Queue(size)
        self.sum = 0

    def next(self, val):
        
     
        if self.queue.qsize() == self.size:
            dequeue_value = self.queue.get()
            self.sum = self.sum - dequeue_value

        self.queue.put(val)
        self.sum += val

        return float(self.sum/self.queue.qsize())
    
"""

from collections import deque
class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.total = 0
        self.size = size

    def next(self, val):
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()
        self.total += val
        return (self.total / len(self.queue))


"""
By definition of the moving window, at each step,
we add a new element to the window, and at the same time we remove
the oldest element from the window.
Here, we could apply a data structure called double-ended queue (a.k.a deque)
to implement the moving window,
which would have the constant time complexity
(\mathcal{O}(1)O(1)) to add or remove an element from both its ends.
With the deque, we could reduce the space complexity down to
\mathcal{O}(N)O(N) where NN is the size of the moving window.
"""

"""
Algorithm

Here is the definition of the deque from Python.
We have similar implementation of deque in other programming languages such as Java.

Deques are a generalization of stacks and queues
(the name is pronounced deck and is short for double-ended queue).
Deques support thread-safe, memory efficient appends
and pops from either side of the deque with approximately the same O(1) performance in either direction.
Follow the intuition, we replace the queue with
the deque and add a new variable window_sum in order to calculate the sum of moving window in constant time.
"""
if __name__ == "__main__":
    window = MovingAverage(3)
    print(window.next(1))
    print(window.next(10))
    print(window.next(3))
    print(window.next(5))
    print(window.queue.qsize())
