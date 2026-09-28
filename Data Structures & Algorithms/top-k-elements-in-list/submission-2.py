class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        res = []
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        
        for num,freq in frequency.items():
            buckets[freq].append(num)
        
        for i in range(len(buckets)-1,0,-1):
            for lst in buckets[i]:
                res.append(lst)
                if len(res) == k:
                    return res