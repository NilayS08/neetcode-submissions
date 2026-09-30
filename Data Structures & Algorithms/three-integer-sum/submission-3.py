class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        res = set()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == target:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif three_sum < target:
                    j += 1
                else:
                    k -= 1
        return [list(num) for num in res]