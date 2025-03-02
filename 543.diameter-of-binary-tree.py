#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0

        def totalheight(root):
            nonlocal diameter
            if not root:
                return 0

            left_height = totalheight(root.left)
            right_height = totalheight(root.right)

            diameter = max(diameter, left_height + right_height)

            return max(left_height, right_height) + 1

        totalheight(root)
        return diameter


# @lc code=end
