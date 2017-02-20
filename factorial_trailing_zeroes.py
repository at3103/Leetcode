class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return n
        #Number of trailing zeroes from number of 10's
        number_of_zeros = (n/10)
        #Number of trailing zeroes from number of 5's
        number_of_zeros += (n+5)/10
        
        #Number of trailing zeroes from number of powers of 5's
        n/=25
        while n:
            number_of_zeros += n
            n/=5
        return number_of_zeros
        