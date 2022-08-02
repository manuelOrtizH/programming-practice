#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/reverse-linked-list/

from node import Node
    
def reverse(head):
    actual = head
    prev = None
    while actual:
        actual.next, prev, actual = prev, actual, actual.next    
    return prev

if __name__ == '__main__':
    llist = head = Node(1)
    llist.append(2)
    llist.append(3)
    llist.display()
    rllist = rhead = reverse(head)
    rllist.display()
    