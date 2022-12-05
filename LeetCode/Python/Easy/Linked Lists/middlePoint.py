# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/middle-of-the-linked-list/description/

from node import Node

class Solution:
    def middleNode(self, head: Node) -> Node:
        slow = fast = head
        while True:
            if not fast or not fast.next: break
            fast = fast.next.next
            slow = slow.next
        return slow