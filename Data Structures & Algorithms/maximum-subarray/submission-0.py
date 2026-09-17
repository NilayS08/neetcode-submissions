class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        largest_sum = nums[0]
        current_sum = nums[0]

        for r in range(1,n):
            current_sum = max(nums[r], current_sum+nums[r])
            largest_sum = max(largest_sum, current_sum)
        
        return largest_sum