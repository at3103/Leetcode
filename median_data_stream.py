"""
Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
"""
from collections import deque

def find_position(arr, x):
    """
    To find the index to insert
    """
    start = 0
    end = len(arr) - 1

    if start == end:
        return int(x >= arr[start])
    while start < end:

        middle = (start + end)/2

        if arr[middle] <= x and arr[middle + 1] > x:
            return middle + 1

        elif arr[middle] > x:
            end = middle - 1
        else:
            start = middle + 1

    return start + int(arr[start] <= x)

class MedianFinder(object):
    """
    Class medianfinder
    """
    __slots__ = ["stream", "operations", "stream_length"]
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stream = deque()
        self.operations = {0 :deque.appendleft, 1: deque.append}
        self.stream_length = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.stream:
            index = 0
        else:
            index = find_position(self.stream, num)

        if index == 0  or index == self.stream_length:
            index = int(index == self.stream_length)
            operation = self.operations[index]
            operation(self.stream, num)
        else:
            self.stream.rotate(self.stream_length - index)
            self.stream.append(num)
            self.stream.rotate(-1 * (self.stream_length - index))
        self.stream_length += 1

    def findMedian(self):
        """
        :rtype: float
        """
        median_index = self.stream_length/2
        if self.stream_length % 2:
            return self.stream[median_index] + 0.0
        else:
            return float(self.stream[median_index] + self.stream[median_index - 1])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
