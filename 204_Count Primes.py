"""
Description:

Count the number of prime numbers less than a non-negative number, n.

"""

import math
from functools import reduce
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 0
        non_prime_nos = [0 for i in range(n)]
        non_prime_nos[0] = 1
        non_prime_nos[1] = 1
        sqrt_n = int(math.sqrt(n)) + 1
        
        for i in range(2,sqrt_n):
            if non_prime_nos[i]:
                continue
            for j in range(2*i,n,i):
                non_prime_nos[j] = 1
        return reduce(lambda acc,x: acc+(x==0),non_prime_nos,0)