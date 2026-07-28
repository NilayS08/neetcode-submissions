class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]: 
        heap = []
        while points:
            coordinates = points.pop()
            x, y = coordinates[0], coordinates[1]
            distance = (x**2) + (y**2)
            heapq.heappush(heap, (-distance,coordinates))
            if len(heap) > k:
                heapq.heappop(heap)
        return [p for _,p in heap]
        
