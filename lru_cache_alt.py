"""
LRU Cache with O(1)
"""
from collections import defaultdict

class LRUCache(object):
    """
    Class for LRU cache
    """
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.lru_dict = defaultdict()
        self.length = 0
        self.index_cache = defaultdict(list)
        self.index_cache[-1] = [-1, -1]
        self.last_key = -1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value = self.lru_dict.get(key, -1)

        if value >= 0 and self.last_key != key:
            prev_key = self.index_cache[key][0]
            next_key = self.index_cache[key][1]
            self.index_cache[prev_key][1] = next_key
            self.index_cache[next_key][0] = prev_key
            self.index_cache[self.last_key][1] = key
            self.index_cache[key][0] = self.last_key
            self.last_key = key

        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.lru_dict.get(key, -1) > 0 and self.last_key != key:
            prev_key = self.index_cache[key][0]
            next_key = self.index_cache[key][1]
            self.index_cache[prev_key][1] = next_key
            self.index_cache[next_key][0] = prev_key
            self.length -= 1

        elif self.lru_dict.get(key, -1) > 0:
            self.length -= 1

        elif self.length == self.capacity:
            key_to_delete = self.index_cache[-1][1]
            next_key = self.index_cache[key_to_delete][1]
            self.index_cache[-1][1] = next_key
            self.index_cache[next_key][0] = -1

            if key_to_delete == self.last_key:
                self.last_key = self.index_cache[self.last_key][0]
            del self.index_cache[key_to_delete]
            del self.lru_dict[key_to_delete]
            self.length -= 1

        self.index_cache[self.last_key][1] = key

        if not self.index_cache.get(key):
            self.index_cache[key] = [-1] * 2
        if self.last_key != key:
            self.index_cache[key][0] = self.last_key

        self.last_key = key
        self.lru_dict[key] = value
        self.length += 1



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
