from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for _ in range(len(nums)):
                if nums[i] == nums[i+1]:
                    return True
                else:
                    return False

nums = [1,2,2,1]
s = Solution()
res = s.containsDuplicate(nums)
print(res)

