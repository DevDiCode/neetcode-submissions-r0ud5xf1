# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        q = deque()

        q.append(root)

        result = []

        if not root:           # handle empty tree
            return []

        while q:
            
            right = None
            for _ in range(len(q)):

                node  =  q.popleft()

                right = node

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

            if right:
                result.append(right.val)

        return result