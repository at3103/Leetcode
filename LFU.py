from collections import OrderedDict
class LFUCache(object):

    def __init__(self, capacity):
        """
        
        :type capacity: int
        """
        self.capacity = capacity
        self.curr = 0
        self.count = 0.0
#        self.freq=dict()
#        self.access=dict()
#        self.cache=dict()
        self.freq=OrderedDict()
        self.access=dict()
        self.cache=OrderedDict()
        self.orderedfreq=list()
        #self.history = list()
        #self.history = list()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value = self.cache.get(key,-1) 
        if value >= 0:
            self.count += 0.0001
            self.freq[key] += 1
            self.access[key] = self.count
            self.freq[key] = int(self.freq[key]) + self.count
            self.orderedfreq = sorted(self.freq.items(),key = lambda f:f[1], reverse=True)
        return value


    def add(self, key, value):
        self.cache[key] = value
        self.count += 0.0001
        self.access[key] = self.count
        self.freq[key] = self.count
        self.orderedfreq = sorted(self.freq.items(),key = lambda f:f[1], reverse=True)
        #self.orderedfreq.append((key,self.count))


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        
        if self.cache.get(key,-1) != -1:
            self.cache[key] = value
            self.count += 0.0001
            self.access[key] = self.count
            self.freq[key] += 1
            self.freq[key] = int(self.freq[key]) + self.count
            self.orderedfreq = sorted(self.freq.items(),key = lambda f:f[1], reverse=True)
        else:
            if self.curr != self.capacity:
                self.curr += 1
                self.add(key,value)
                
            else:
                keyrem = int(self.orderedfreq[self.curr-1][0])
                del(self.cache[keyrem])
                del(self.access[keyrem])
                del(self.freq[keyrem])
                self.add(key,value)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)