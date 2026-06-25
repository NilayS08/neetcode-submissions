class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        res = []
        
        for i in range(k):
            heapq.heappush(maxHeap, (-nums[i],i))
        res.append(-maxHeap[0][0])
        
        l = 0
        for r in range(k, len(nums)):
            heapq.heappush(maxHeap, (-nums[r],r))
            while maxHeap[0][1] <= l:
                heapq.heappop(maxHeap)
            res.append(-maxHeap[0][0])
            l += 1
        return res