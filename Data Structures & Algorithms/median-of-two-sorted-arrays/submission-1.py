class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        l,r = 0,len(nums) - 1

        if len(nums) % 2 != 0:
            mid = (l+r) // 2
            return nums[mid]
        else:
            mid1 = (l+r) // 2
            mid2 = mid1 + 1
            return (nums[mid1] + nums[mid2]) / 2
