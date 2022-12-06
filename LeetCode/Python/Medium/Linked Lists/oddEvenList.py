# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/odd-even-linked-list/description/

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        evenList = even

        while (even and even.next):
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
            
        odd.next = evenList
        return head