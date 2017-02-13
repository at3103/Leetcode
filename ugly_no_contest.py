"""
Ugly number_264
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only
include 2, 3, 5. For example, 6, 8 are ugly while 14 is not
ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.


"""
def check_and_reduce_divisibility(number, prime_factor):
    """
    function to check for divisibility and if divisible reduce
    """
    while not number%prime_factor:
        number /= prime_factor
    return number

class Solution(object):
    """
    Class for Solution
    """
    @classmethod
    def isUgly(cls, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        for i in [2, 3, 5]:
            num = check_and_reduce_divisibility(num, i)
            if num == 1:
                return True
        return False
