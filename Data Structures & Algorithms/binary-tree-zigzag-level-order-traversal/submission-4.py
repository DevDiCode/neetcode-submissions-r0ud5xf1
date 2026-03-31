# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        response = []
        level = 0
        
        while q:
            size = len(q)
            curr = []
            
            for _ in range(size):
                node = q.popleft()
                curr.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Reverse for odd levels (1, 3, 5...)
            if level % 2 == 1:
                curr.reverse()
            
            response.append(curr)
            level += 1
        
        return response

        