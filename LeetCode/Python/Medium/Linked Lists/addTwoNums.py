#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/add-two-numbers/

from node import Node

class Solution:
    def addTwoNumbers(self, l1, l2):
        digits = []
        head_result = Node(-1)
        actual = head_result
        n1, n2 = l1, l2
        s = False
        i = 0
        while n1 or n2:
            a = n1.val if n1 else 0
            b = n2.val if n2 else 0
            n = a+b+s
            m = n%10
            actual.next = Node(m)
            s = n!=m 
            n1, n2 = n1 and n1.next, n2 and n2.next
            actual = actual.next
            i+=1
            
        if s: actual.next = Node(1)

        return head_result.next