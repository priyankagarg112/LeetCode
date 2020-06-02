'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        head=root
        self._invert(head)
        
        return root
    
    def _invert(self,head):
        if not head:
            return
        head.left,head.right=head.right,head.left
        self._invert(head.left)
        self._invert(head.right)
        
