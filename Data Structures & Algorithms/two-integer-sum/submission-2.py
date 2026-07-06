# corrected return statement
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visitedMap = {} 
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in visitedMap:
                return [visitedMap[diff],i]
            visitedMap[n] = i
        return 0