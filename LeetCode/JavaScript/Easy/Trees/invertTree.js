// Manuel Ortiz at 2022
// Extracted from: https://leetcode.com/problems/invert-binary-tree/

const invertTree = (root) => {
    if (root == null) return null;
    const left = root.left;
    const right = root.right;
    
    root.left = invertTree(right);
    root.right = invertTree(left);
    
    
    return root;

};