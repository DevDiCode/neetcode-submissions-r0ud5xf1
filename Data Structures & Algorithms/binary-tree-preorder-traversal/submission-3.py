# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:


        # self.response = []


        # def helper(node):

        #     if not node:
        #         return 
        #     self.response.append(node.val)
        #     helper(node.left)
        #     helper(node.right)
        

        # helper(root)
        # return self.response
        stack = []
        result = []

        if root:
            stack.append(root)

        while stack:

            node = stack.pop()

            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:

                stack.append(node.left)

        return result






                
        