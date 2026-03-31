class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def helper(node):
            if not node:
                return TreeNode(val)
            if val < node.val:
                node.left = helper(node.left)   # attach to left child
            else:
                node.right = helper(node.right) # attach to right child
            return node

        return helper(root)