# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        self.response = []

        # def helper(root):

        #     if not root:
        #         return
            

        #     helper(root.left)

        #     self.response.append(root.val)

        #     helper(root.right)
        

        # helper(root)

        # return self.response


        stack = []
        response = []

        curr = root

        while curr or stack :


            while  curr:
                stack.append(curr)
                curr = curr.left
        
            curr = stack.pop()
            response.append(curr.val)

            curr = curr.right



        return response






