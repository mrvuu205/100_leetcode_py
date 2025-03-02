#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isSameTree(q, p):
            if not p and not q:
                return True

            if (q and not p) or (p and not q):
                return False

            if q.val != p.val:
                return False

            return isSameTree(p.right, q.left) and isSameTree(p.left, q.right)

        return isSameTree(root.left, root.right)


# @lc code=end
