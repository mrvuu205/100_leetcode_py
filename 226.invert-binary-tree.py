#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap_root(root):
            if root is None:
                return

            root.left, root.right = root.right, root.left

            swap_root(root.left)
            swap_root(root.right)

        swap_root(root)
        return root


# @lc code=end
