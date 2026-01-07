class Solution:
    def findMin(self, nums):
        start, end = 0, len(nums)-1
        while start < end:
            mid = (start+end)//2
            # Checking and moving to second half
            if nums[mid]>nums[end]:
                start = mid+1
            else:
                end = mid # Moving to first half
        return nums[start]
sol = Solution()
print(sol.findMin([3,4,5,1,2]))