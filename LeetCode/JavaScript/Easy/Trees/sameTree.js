// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/same-tree/


import { Node } from './node.js';


const isSameTree = (p,q) => {
    
    if (p == null && q == null){
        return true;
    } else if (p == null || q == null) {
        return false;
    }
    
    
    if (p.val != q.val){
        return false;
    }
    
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right) && true;
};

const p = new Node(1);
p.left = new Node(2);
p.right = new Node(3);

const q = new Node(1);
q.left = new Node(2);
q.right = new Node(3);

console.log(isSameTree(p,q));