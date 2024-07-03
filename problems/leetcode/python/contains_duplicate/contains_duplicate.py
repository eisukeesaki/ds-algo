class ContainsDuplicate:
    # O(n^2)
    def brute_force(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for k in range(i+1, len(nums)):
                if nums[i] == nums[k]:
                    return True
        return False
    # O(n)
    def convert_to_sets(self, nums: list[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        return False
    def pre_sort(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


s = ContainsDuplicate()
# print(s.brute_force([1,2,3,0]))
# print(s.convert_to_sets([1,2,3,0,2]))
print(s.pre_sort([1,2,3,0,0]))
        
