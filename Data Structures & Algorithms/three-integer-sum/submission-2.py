class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. brute force - n3 / 1
        # 2. sort, i, 2 pointer - n2 / 1
        target = 0
        nums.sort()
        res = set()
        i=0
        for i in range(len(nums)):
            j,k=i+1,len(nums)-1
            while j<k:
                r = nums[i]+nums[j]+nums[k]
                if r == target:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif r<target:
                    j+=1
                else:
                    k-=1
        return [list(r) for r in res]
        