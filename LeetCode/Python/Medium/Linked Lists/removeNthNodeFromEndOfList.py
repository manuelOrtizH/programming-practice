# Manuel Ortiz at 2024
# Extracted from: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from node import Node

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        i = 0

        while i < n: 
            fast = fast.next
            i+=1

        if not fast: return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head
