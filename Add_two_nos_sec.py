# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getNumber(l):
    n=0
    while l!=None:
        n = n * 10 + l.val 
        l = l.next
    return n
    
def getList(n):
    l = ListNode(0)
    while n:
        l.val += n%10
        n/=10
        temp = ListNode(0)
        temp.next = l
        l = temp
    return l.next
    
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.val == 0:
            return l2
        if l2.val == 0:
            return l1
        number = getNumber(l1) + getNumber(l2)
        l3 = getList(number)
        return l3