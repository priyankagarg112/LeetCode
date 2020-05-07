'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.



Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#TreeNode{val: 1, left: TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: None},right: TreeNode{val: 3, left: None, right: None}}

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        res1 = self.get_elems(root,x,0,root.val)
        res2 = self.get_elems(root,y,0,root.val)
        if res1[0] == res2[0] and res1[1] != res2[1]:
            return True
        return False


    def get_elems(self,root,x,level,par):
        if root is None:
            return (-1,-1)
        if root.val == x:
            return (level,par)
        out = self.get_elems(root.left,x,level+1,root.val)
        if out[0] !=-1:
            return out
        out = self.get_elems(root.right,x,level+1,root.val)
        return out

