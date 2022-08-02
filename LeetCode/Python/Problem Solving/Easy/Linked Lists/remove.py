#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/remove-linked-list-elements/
from re import A
from node import Node

def remove_elements(head, data):
    #Moving the head until there is a valid head
    while head and head.data == data:
        head = head.next
        
    if not head:
        return head
    
    actual = head

    while actual.next:
        if actual.next.data == data:
            actual.next = actual.next.next
        else:
            actual = actual.next

    return head 

if __name__ == '__main__':
    llist = head = Node(1)
    head.append(1,2,3,4,1,4,2)
    llist.display()
    llist = head = remove_elements(head, 1)
    if llist:
        llist.display()
    else:
        print([])


