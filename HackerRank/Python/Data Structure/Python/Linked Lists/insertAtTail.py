#Manuel Ortiz Hernández at 2020
#Linked Lists. Extracted from: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def printSinglyLinkedList(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

def insertNodeAtTail(head, data):
    return head
                
            
if __name__ == '__main__':
    
    llist_count = int(input())
    llist = SinglyLinkedList()
    print('--------\n')

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    printSinglyLinkedList(llist.head, '\n')
    

    
