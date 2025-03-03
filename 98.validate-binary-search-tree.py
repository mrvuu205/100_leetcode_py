#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # def validBST(node, low=float("-inf"), hight=float("inf")):

        #     if not node:
        #         return True

        #     if (node.val <= low) or (node.val >= hight):
        #         return False

        #     return validBST(node.left, low, node.val) and validBST(
        #         node.right, node.val, hight
        #     )

        # return validBST(root)

        # prev = [float("-inf")]

        # def inorder(node):

        #     if not node:
        #         return True

        #     if not inorder(node.left):
        #         return False

        #     if node.val <= prev[0]:
        #         return False
        #     prev[0] = node.val

        #     return inorder(node.right)

        # return inorder(root)

        prev = float("-inf")
        curr = root
        stack = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if curr.val <= prev:
                return False
            prev = curr.val

            curr = curr.right

        return True


# @lc code=enk
