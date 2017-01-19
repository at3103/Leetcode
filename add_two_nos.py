# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = l1
        while l2 != None or l3 != None:
            if l2 !=None:
                l3.val += l2.val
            if l3.next == None and l3.val/10 != 0:
                l3.next=ListNode(l3.val/10)
            elif l3.next != None:
                l3.next.val += l3.val/10
            elif l3.next == None and l2 != None:
                l3.next = l2.next
                break
            l3.val = l3.val%10
            l3 = l3.next
            if l2:
                l2=l2.next
        return l1