class Solution:
    def containsDuplicate(self, nums):
        if len(set(nums))< len(nums):
            return True
        return False
array = [1,2,3,1]
sol = Solution()
print(sol.containsDuplicate(array))