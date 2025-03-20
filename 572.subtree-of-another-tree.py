#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # def check sametree
        def isSameTree(p, q):

            if not q and not p:
                return True

            if (p and not q) or (q and not p):
                return False

            if p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        # def check root = subroot
        def has_subtree(root):

            if not root:
                return False

            if isSameTree(root, subRoot):
                return True

            return has_subtree(root.left) or has_subtree(root.right)

        return has_subtree(root)


# @lc code=end
