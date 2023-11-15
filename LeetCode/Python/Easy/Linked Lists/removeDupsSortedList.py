# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from node import Node

class Solution:
    def deleteDuplicates(self, head: Node) -> Node:
        if not head or not head.next: 
            return head
        
        curr = head
        while curr.next:
            if curr.data == curr.next.data: 
                curr.next = curr.next.next
            else: 
                curr = curr.next
        return head


if __name__ == '__main__':
    l_list = head = Node(1)
    head.append(1,2,3,3)
    head.display()
    obj = Solution()
    res = obj.deleteDuplicates(head)
    res.display()

    