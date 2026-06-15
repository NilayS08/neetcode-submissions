class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n-1
        max_area = 0
        
        while i < j:
            if heights[i] >= heights[j] :
                curr_area = min(heights[i],heights[j])*(j-i)
            if heights[i] < heights[j]:
                curr_area = min(heights[i],heights[j])*(j-i)
                i += 1
            else:
                j -= 1
            max_area = max(max_area,curr_area)
            
        return max_area
