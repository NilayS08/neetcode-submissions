class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visitedMap = {} 
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in visitedMap:
                return [nums.index(diff),i]
            visitedMap[n] = i
        return 