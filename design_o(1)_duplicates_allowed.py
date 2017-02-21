"""
Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements.
The probability of each element
being returned is linearly related to the number of same value the collection contains.
"""

from collections import defaultdict, deque
import random

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.collection = defaultdict(int)
        self.collection_index = defaultdict(list)
        self.stream = deque()
        self.last_index = -1

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        
        return_value = self.collection.get(val, -1) == -1
        self.collection[val] += 1
        self.last_index += 1
        self.stream.append(val)
        self.collection_index[val].append(self.last_index)

        return return_value
            

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        return_value = self.collection.get(val, -1) != -1
        
        if return_value:
            if self.collection.get(val, -1) == 1:
                del self.collection[val]
            else:
                self.collection[val] -= 1
            
            last_element = self.stream[-1]
            
            index_to_swap = self.collection_index[val].pop() % (self.last_index + 1)
            
            if last_element != val:
                self.collection_index[last_element].pop()
                self.collection_index[last_element].append(index_to_swap)
                self.stream[-1], self.stream[index_to_swap] = self.stream[index_to_swap], self.stream[-1]
            self.stream.pop()
            self.last_index -= 1
        return return_value

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        
        random_index = random.randint(0,self.last_index)
        
        return self.stream[random_index]



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()