class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count_map = {}

        #Counter hardcoded
        for i in nums:
            count_map[i] = 1+count_map.get(i,0)
        
        #bucket sorting
        bucket = [[] for i in range(n+1)]

        for key,val in count_map.items():
            bucket[val].append(key)
        
        result = []
        for i in range(len(bucket)-1,0,-1):
            for lst in bucket[i]:
                result.append(lst)
                if len(result)==k:
                    return result