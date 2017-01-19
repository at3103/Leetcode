def getNumber(num):
    n=0
    for i in num:
        n = n * 10 + int(i)
    return n

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        number = getNumber(num1) + getNumber(num2)
        return str(number)