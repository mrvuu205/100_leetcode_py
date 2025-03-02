#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # tao defaultdict list
        # duyet qua tung tu cua mang strs
        # neu trung key thi se append tu do vao defaultdict key
        # neu khong trung thi key do bang rong

        ans = defaultdict(list)

        # for s in strs:
        #     key = "".join(sorted(s))
        #     ans[key].append(s)

        # return list(ans.values())

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            ans[key].append(s)

        return ans.values()


# @lc code=end
