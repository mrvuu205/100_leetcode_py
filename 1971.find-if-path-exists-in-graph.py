#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#
from collections import defaultdict


# @lc code=start
class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        seen.add(source)

        def dfs(i):
            if i == destination:
                return True

            for neight in graph[i]:
                if neight not in seen:
                    seen.add(neight)
                    if dfs(neight):
                        return True

            return False

        return dfs(source)


# @lc code=end
