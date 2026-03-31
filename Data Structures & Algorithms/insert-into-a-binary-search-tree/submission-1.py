
# Insert into a Binary Search Tree (LeetCode 701)
# ----------------------------------------------
# Given the root of a BST and a value to insert,
# return the root of the BST after insertion, ensuring BST properties remain valid.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------
# 1. Exploration / Understanding
# ------------------------------------------------
# - In a BST, left subtree values < node.val, right subtree values > node.val.
# - To insert:
#     * If tree is empty -> new node becomes root.
#     * Otherwise, find correct position where left/right child is None
#       and attach the new node there.
# - Preserve BST property.

# ------------------------------------------------
# 2. Brainstorm Approaches
# ------------------------------------------------
# A) Recursive DFS (chosen)
#    - Base: if current node is None -> create new node and return it.
#    - Compare `val` with current node's value:
#         - If smaller -> recurse into left subtree and attach result to node.left
#         - If bigger  -> recurse into right subtree and attach result to node.right
#    - Return current node on each call.
#
# B) Iterative
#    - Walk down from root until a None child is found, attach there.
#    - Slightly faster in Python due to no recursion overhead, but less concise.

# We'll implement both for completeness.

# ------------------------------------------------
# 3. Plan (Recursive)
# ------------------------------------------------
# 1. If root is None => Tree empty => return new TreeNode(val)
# 2. If val < root.val:
#       root.left = insertIntoBST(root.left, val)
#    Else:
#       root.right = insertIntoBST(root.right, val)
# 3. Return root after updating.

class Solution:
    # Recursive version
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    # Iterative version
    def insertIntoBST_iterative(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr = root
        while True:
            if val < curr.val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right
        return root


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

# ------------------------------------------------
# 4. Edge Cases
# ------------------------------------------------
# - Empty tree: should return a new node as root.
# - Insert smaller than all existing nodes: becomes leftmost child.
# - Insert larger than all existing nodes: becomes rightmost child.
# - Tree is skewed left or skewed right: still works.
# - Duplicate values: typically not inserted in BST (problem assumes unique values).

# ------------------------------------------------
# 5. Complexity Analysis
# ------------------------------------------------
# Let h = height of the tree, n = number of nodes.
# - Time: O(h)
#     * Balanced tree: O(log n)
#     * Worst (skewed): O(n)
# - Space:
#     * Recursive: O(h) call stack
#     * Iterative: O(1) extra space

# ------------------------------------------------
# 6. Test Cases (commented for easy enabling)
# ------------------------------------------------
# root = TreeNode(4)
# root.left = TreeNode(2, TreeNode(1), TreeNode(3))
# root.right = TreeNode(7)
# s = Solution()
# # Recursive insert
# root = s.insertIntoBST(root, 5)
# print(root.right.left.val)  # Expected: 5
# # Iterative insert
# root = s.insertIntoBST_iterative(root, 6)
# print(root.right.left.right.val)  # Expected: 6
