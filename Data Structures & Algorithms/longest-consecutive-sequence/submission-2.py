class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        res = 0
        
        for num in set_nums:
            if num-1 not in set_nums:
                current = num
                length = 1
                while current+1 in set_nums:
                    current += 1
                    length += 1
                res = max(res,length)
        return res