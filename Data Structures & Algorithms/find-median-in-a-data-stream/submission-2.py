# Naive Approach
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap:
            heapq.heappush(self.maxHeap, -num)

        elif num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            temp = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, temp)
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            temp = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -temp)
        
        if self.maxHeap and self.minHeap and (-self.maxHeap[0] > self.minHeap[0]):
            left = -heapq.heappop(self.maxHeap)
            right = heapq.heappop(self.minHeap)

            heapq.heappush(self.maxHeap, -right)
            heapq.heappush(self.minHeap, left)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        elif len(self.maxHeap) == len(self.minHeap):
            return ((-self.maxHeap[0]) + self.minHeap[0]) / 2
        return self.minHeap[0]