#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#


# @lc code=start
class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        d = self.trie

        for _ in word:
            if _ not in d:
                d[_] = {}
            d = d[_]

        d["."] = "."

    def search(self, word: str) -> bool:
        d = self.trie

        for _ in word:
            if _ not in d:
                return False
            d = d[_]

        return "." in d

    def startsWith(self, prefix: str) -> bool:
        d = self.trie

        for _ in prefix:
            if _ not in d:
                return False
            d = d[_]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
