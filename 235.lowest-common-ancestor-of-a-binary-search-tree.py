#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        # if not root:
        #     return

        # if root.val < q.val and root.val < p.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # elif root.val > q.val and root.val > p.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # else:
        #     return root

        curr = root

        while curr:
            curr_val = curr.val

            if curr_val < q.val and curr_val < p.val:
                curr = curr.right
            elif curr_val > q.val and curr_val > p.val:
                curr = curr.left
            else:
                return curr


# @lc code=end
