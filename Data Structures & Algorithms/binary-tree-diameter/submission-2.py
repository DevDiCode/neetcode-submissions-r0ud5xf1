# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        

        self.dia = 0 


        def helper(node):


            if not node:
                return 0 
            

            left = helper(node.left)

            right = helper(node.right)

            self.dia  = max(self.dia, left+right)

            return 1+ max(left,right)

        helper(root)
        return self.dia