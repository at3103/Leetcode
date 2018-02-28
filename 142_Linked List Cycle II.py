"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cycle_nodes = set()
        
        if not head or not head.next:
            return None
        slow = head
        fast = head.next
        
        while fast:
            
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next if fast.next else None
        
        if not fast:
            return None

        while slow not in cycle_nodes:
            cycle_nodes.add(slow)
            slow = slow.next

        
        slow = head
        
        while slow:
            if slow in cycle_nodes:
                break
            slow = slow.next
                
        return slow
        