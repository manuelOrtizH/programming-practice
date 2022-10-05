# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2 or None
        
        node = final_list = ListNode(-1) #Dummy Node
        node1 = list1
        node2 = list2
            
        while node1 and node2:
            if node1.val < node2.val:
                node.next = ListNode(node1.val)
                node = node.next
                node1 = node1.next
            else:
                node.next = ListNode(node2.val)
                node = node.next
                node2 = node2.next
    
        node.next = node2 if not node1 else node1
        
        
        return final_list.next