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

if __name__ == "__main__":
    window = MovingAverage(3)
    print(window.next(1))
    print(window.next(10))
    print(window.next(3))
    print(window.next(5))
    print(window.queue.qsize())
