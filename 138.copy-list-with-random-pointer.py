#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        hash_map = {}
        copy = head

        while copy:
            hash_map[copy] = Node(copy.val)
            copy = copy.next

        copy = head
        while copy:
            if copy.next:
                hash_map[copy].next = hash_map[copy.next]
            if copy.random:
                hash_map[copy].random = hash_map[copy.random]
            copy = copy.next

        return hash_map[head]


# @lc code=end
