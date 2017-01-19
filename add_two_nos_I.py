# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getNumber(l):
    n=0
    c = 0
    while l!=None:
        n = l.val * 10**c + n
        c+=1
        l = l.next
    return n
    
def getList(n):
    l = ListNode(0)
    temp = l
    while n:
        l.val += n%10
        n/=10
        if n:
            l.next = ListNode(0)
            l = l.next
    return temp


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        number = getNumber(l1) + getNumber(l2)
        l3 = getList(number)
        return l3
        