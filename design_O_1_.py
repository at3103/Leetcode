from collections import defaultdict
class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_struct = defaultdict()
        self.counter_struct = defaultdict(set)
        self.max_count = 0
        self.min_count = 0

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        old_count = 0

        if self.data_struct.get(key):
            old_count = self.data_struct[key]
            new_count = old_count + 1
            self.counter_struct[old_count] -= {key}
            self.data_struct[key] += 1
        else:
            self.data_struct[key] = 1
            new_count = 1
            self.min_count = 1
        
        #Clean up 
        if self.counter_struct.get(old_count, -1) == set():
            del self.counter_struct[old_count]
        
        #If this is the new maximal value, incrementing the max_count
        if new_count > self.max_count:
            self.max_count += 1
        
        #Adding the new key to its appropriate counter_struct
        self.counter_struct[new_count].add(key)
        
        #If this is the new minimal value, decrementing the max_count
 #       if self.counter_struct.get(self.min_count, -1) == -1:# or self.counter_struct.get(self.min_count, -1) == set():
 #           self.min_count += 1


    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if not self.data_struct.get(key):
            return 

        old_count = self.data_struct[key]
        self.counter_struct[old_count] -= {key}
        if self.data_struct.get(key) > 1:
            new_count = old_count - 1
            self.data_struct[key] -= 1
        else:
            del self.data_struct[key]
            new_count = 0
            
        #If this is the new maximal value, incrementing the max_count
        if not self.counter_struct.get(self.max_count):
            self.max_count -= 1
        
        
        if new_count:    
        #Adding the new key to its appropriate counter_struct
            self.counter_struct[new_count].add(key)


    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        maximal_key = ""
        if self.counter_struct.get(self.max_count):
            maximal_key = self.counter_struct.get(self.max_count).pop()
            self.counter_struct[self.max_count].add(maximal_key)
        return maximal_key

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        minimal_key = ""
        #If this is the minimal value, find the next_minimal value. Amortized cost would would be O(1)
        if self.counter_struct.get(self.min_count, -1) == -1 or self.counter_struct.get(self.min_count, -1) == set():
            for count in range(2,self.max_count + 1):
                if self.counter_struct.get(count):
                    self.min_count = count
                    break
        if self.counter_struct.get(self.min_count):
            minimal_key = self.counter_struct.get(self.min_count).pop()
            self.counter_struct[self.min_count].add(minimal_key)
        return minimal_key        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()