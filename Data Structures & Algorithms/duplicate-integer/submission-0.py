class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_num = nums.sort()
        n = len(nums)
        for i in range(0,n-1):
            if nums[i] == nums[i+1]:
                return True
        return False
            