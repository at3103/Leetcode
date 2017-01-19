from collections import OrderedDict
class LFUCache(object):

    def __init__(self, capacity):
        """
        
        :type capacity: int
        """
        self.capacity = capacity
        self.curr = 0
        self.count = 0.0
        self.freq=dict()
        self.cache=dict()
        self.orderedfreq=list()
        self.min = 0
        self.revfreq=dict()


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value = self.cache.get(key,-1) 
        if value >= 0:
            self.count += 0.0001
            self.freq[key] += 1
            self.freq[key] = int(self.freq[key]) + self.count
            self.revfreq[self.freq[key]] = key
            #self.orderedfreq = sorted(self.freq.items(),key = lambda f:f[1], reverse=True)
            self.min = self.revfreq[min(self.freq.values())]
        return value


    def add(self, key, value):
        self.cache[key] = value
        self.count += 0.0001
        self.freq[key] = self.count
        self.revfreq[self.freq[key]] = key
        self.min = self.revfreq[min(self.freq.values())]
        #self.orderedfreq = sorted(self.freq.items(),key = lambda f:f[1], reverse=True)

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
            self.freq[key] += 1
            self.freq[key] = int(self.freq[key]) + self.count
            self.revfreq[self.freq[key]] = key
            self.min = self.revfreq[min(self.freq.values())]
            #self.orderedfreq = sorted(self.freq.items(),key = lambda f:f[1], reverse=True)
        else:
            if self.curr != self.capacity:
                self.curr += 1
                self.add(key,value)
                
            else:
                #keyrem = int(self.orderedfreq[self.curr-1][0])
                keyrem=self.min
                del(self.revfreq[self.freq[keyrem]])
                del(self.cache[keyrem])
                del(self.freq[keyrem])
                self.add(key,value)
                #self.orderedfreq = sorted(self.freq.items(),key = lambda f:f[1], reverse=True)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)