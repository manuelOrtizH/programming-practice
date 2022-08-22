import { Node } from './node.js';

const reverseList = head => {
    let currentNode = head;
    let prev = null;
    
    while (currentNode != null){
        [currentNode.next, prev, currentNode] = [prev, currentNode, currentNode.next];
    }
    
    return prev;
    
};

let head = new Node(5)
head.append(4,3,2,1)
head.display();
head = reverseList(head);
head.display();