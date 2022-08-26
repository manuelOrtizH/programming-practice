import { Node } from '../../Easy/Linked Lists/node.js';


const copyRandomList = head => {
    
};

const head = new Node(7);
const node1 = new Node(13);
const node2 = new Node(11);
const node3 = new Node(10);
const node4 = new Node(1);

head.next = node1;
node1.next = node2;
node2.next = node3;
node3.next = node4;

head.random = node3.next;
node1.random = head;
node2.random = node4;
node3.random = node2;
node4.random = head;

head.display()