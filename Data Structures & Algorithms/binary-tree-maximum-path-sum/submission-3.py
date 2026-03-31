class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")  # Global maximum path sum

        def dfs(node):
            if not node:
                return 0

            # 1️⃣ Postorder Recursion — get max gain from left and right
            left_gain = max(0, dfs(node.left))   # Ignore if < 0
            right_gain = max(0, dfs(node.right))

            # 2️⃣ Current node is turning point — local path sum
            current_path_sum = node.val + left_gain + right_gain

            # 3️⃣ Update global max if this path is the best so far
            self.max_sum = max(self.max_sum, current_path_sum)

            # 4️⃣ Return path sum including current node + max subpath (for parent usage)
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum
