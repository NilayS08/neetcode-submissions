class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}

        for i,num in enumerate(nums):
            if target - num in seen:
                return [seen[target-num],i]
            seen[nums[i]] = i   