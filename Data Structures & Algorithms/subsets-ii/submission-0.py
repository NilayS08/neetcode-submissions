class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        def backtrack(i, sol):
            if i == n:
                res.append(sol[:])
                return
            sol.append(nums[i])
            backtrack(i+1, sol)
            sol.pop()
            while i < n-1 and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, sol)
        
        backtrack(0, [])
        return res