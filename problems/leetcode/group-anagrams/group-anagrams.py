from typing import List

###############################################################################

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for string in strs:
            res.append(string)
        return res

###############################################################################

strs = ["eat","tea","tan","ate","nat","bat"]

solution = Solution()
result = solution.groupAnagrams(strs)

print(result)
