#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/intersection-of-two-linked-lists/

from node import Node

def create_intersection():
    llistA = headA = Node(4)
    llistA.append(1)
    llistB = headB = Node(5)
    llistB.append(6,1)

    llistC = headC = Node(8)
    llistC.append(4,5)

    llists = [llistA, llistB]
    for llist in llists:
        actual = llist
        while actual.next:
            actual = actual.next
        actual.next = headC
    return llistA,llistB
            

def get_intersection_node(headA, headB):
    nodes = []
    actualA = headA
    nodes = set()
    while actualA:
        nodes.add(actualA)
        actualA = actualA.next
    actualB = headB
    while actualB not in nodes or not actualB:
        actualB = actualB.next

    return actualB


    

if __name__ == '__main__':
    llistA, llistB = create_intersection()
    llistA.display(), llistB.display()


    node_intersected = get_intersection_node(llistA, llistB)
    print(f'The intersection is in node: {node_intersected.data}' if node_intersected else 'No intersection')