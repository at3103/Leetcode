"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

"""

from functools import reduce
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ham_d = 0
        xbin = bin(x)[2:]
        ybin = bin(y)[2:]
        xstrt = 0
        ystrt = 0
        
        if len(xbin) > len(ybin):
            xstrt = len(xbin) - len(ybin)
            ybin = '0'*xstrt + ybin
        elif len(xbin) < len(ybin):
            ystrt = len(ybin) - len(xbin)
            xbin = '0'*ystrt + xbin
        
        
        return reduce(lambda acc, tup: acc + int(tup[0] != tup[1]), zip(xbin,ybin), ham_d)
