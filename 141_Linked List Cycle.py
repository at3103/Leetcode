"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = head
        fast = head.next.next if head.next else None
        
        while fast:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next if fast.next else None
        
        return False