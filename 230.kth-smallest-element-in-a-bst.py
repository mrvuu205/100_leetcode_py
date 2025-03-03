#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # count = [k]
        # ans = [0]

        # def dfs(node):

        #     if not node:
        #         return

        #     dfs(node.left)

        #     if count[0] == 1:
        #         ans[0] = node.val

        #     count[0] = count[0] - 1

        #     if count[0] > 0:
        #         dfs(node.right)

        # dfs(root)
        # return ans[0]

        # res = []

        # def inorder(node):

        #     if not node:
        #         return

        #     inorder(node.left)
        #     res.append(node.val)
        #     inorder(node.right)

        # inorder(root)
        # return res[k - 1]

        # res = [None]
        # count = [0]

        # def inorder(node):

        #     if not node or res[0] is not None:
        #         return

        #     inorder(node.left)

        #     count[0] += 1

        #     if count[0] == k:
        #         res[0] = node.val
        #         return
        #     inorder(node.right)

        # inorder(root)
        # return res[0]

        stack = []
        curr = root
        count = 0

        while curr or stack:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            count += 1

            if count == k:
                return curr.val

            curr = curr.right


# @lc code=end
