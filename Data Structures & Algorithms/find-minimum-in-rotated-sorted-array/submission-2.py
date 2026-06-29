class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_val = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                min_val = min(min_val,nums[l])
                break
            
            k = (l+r) // 2
            min_val = min(min_val,nums[k])
            
            if nums[k] >= nums[l]:
                l = k + 1
            else:
                r = k - 1
        return min_val
                