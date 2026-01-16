class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n

        # Step 1: Prefix products
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Step 2: Postfix products
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

sol = Solution()
arr= [-1,1,0,-3,3]
print(sol.productExceptSelf(arr))