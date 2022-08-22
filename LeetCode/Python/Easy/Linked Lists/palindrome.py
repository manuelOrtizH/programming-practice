#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/palindrome-linked-list/

from node import Node

def palindrome(head):
    #Getting the length one by one
    actual_node = head
    length = head.length()
    prev_node = None
    mid = length//2
    i = 0
    while i <= mid:
        actual_node.next, prev_node, actual_node = prev_node, actual_node, actual_node.next
        i+=1
    left_head = prev_node #is reversed
    right_head = actual_node if length % 2 == 0 else actual_node.next
    while right_head:
        if left_head.data != right_head.data:
            return False
        left_head, right_head = left_head.next, right_head.next
        i+=1
    return True

#With "Runner Technique"
def _palindrome(head):
    #Reach to the middle of the linked list, wether is a odd or even length
    # 1->2->3->2->1
    # 3 would be the middle, but does not matter to verify if it is palindrome
    # What we care, is about the 1,2 and 2,1 Nodes
    slow = fast = head
    #Finding the middle point
    while True:
        if not fast or not fast.next: break
        fast = fast.next.next
        slow = slow.next
    
    middle = slow.next if fast else slow
    if not middle:
        return True
    prev = None
    actual = middle
    #Reversing the second half of the linked list
    while actual:
        actual.next, prev, actual = prev, actual, actual.next 
    
    actual = head
    while prev:
        if actual.data != prev.data:
            return False
        actual = actual.next
        prev = prev.next


    return True

if __name__ == '__main__':
    llist = head = Node(1)
    llist.append(2,2,1)
    result = _palindrome(head)
    print(result)
    