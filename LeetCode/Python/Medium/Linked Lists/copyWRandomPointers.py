# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/copy-list-with-random-pointer/description/


from node import Node

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        nodes_dict = dict()
        actual_node = head

        # First iteration over the original Linked list
        while actual_node:
            nodes_dict[actual_node] = Node(actual_node.val)
            actual_node = actual_node.next

        actual_node = head
        #Second iteration over the original Linked List
        while actual_node:
            nodes_dict.get(actual_node).next = nodes_dict.get(actual_node.next)
            nodes_dict.get(actual_node).random = nodes_dict.get(actual_node.random)
            actual_node = actual_node.next

        return nodes_dict.get(head)