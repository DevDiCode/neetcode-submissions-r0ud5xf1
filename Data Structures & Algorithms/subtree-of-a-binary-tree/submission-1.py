# ✅ Problem: Subtree of Another Tree (Leetcode 572)
# Given roots of two binary trees root and subRoot, return True if subRoot
# is a subtree of root: i.e., some node in root whose entire subtree is
# structurally identical to subRoot and has the same node values. [web:58][web:62]

# ---------------------------------------------------------
# 🧠 Pattern: DFS + Same-Tree Check
# - Traverse the big tree (root) with DFS.
# - At each node, check if the subtree starting there is exactly the same
#   as subRoot (using isSameTree). [web:60][web:61]
# ---------------------------------------------------------

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        """
        Edge Cases:
        - subRoot is None  → True (empty tree is a subtree of any tree). [web:62]
        - root is None and subRoot not None → False (no place to match). [web:62]
        - root and subRoot both non-empty → need DFS + exact match check.
        """

        # If subRoot is empty, it's always a subtree.
        if not subRoot:
            return True

        # If main tree is empty but subRoot is not, cannot contain it.
        if not root:
            return False

        # If trees match starting at this node, we're done.
        if self.isSameTree(root, subRoot):
            return True

        # Otherwise, search in left or right subtree.
        return self.isSubtree(root.left, subRoot) or \
               self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        Check if two trees are structurally identical with identical values. [web:60][web:61]
        """

        # Both empty → identical.
        if not p and not q:
            return True

        # One empty, one not → not identical.
        if not p or not q:
            return False

        # Values must match and children must be identical.
        return (
            p.val == q.val and
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )
