class Solution:
    def productExceptSelf(self, nums):
        prefix_product = [""]*len(nums)
        postfix_product = [""]*len(nums)
        res = [""]*len(nums)

        # Adding previous elements product into list
        for i in range(len(nums)):
            if i ==0:
                prefix_product[i]= nums[i]
            else:
                prefix_product[i]= prefix_product[i-1]*nums[i]

        # Adding successor elements product into list
        for j in range(len(nums)-1, -1, -1):
            if j == len(nums)-1:
                postfix_product[j]= nums[j]
            else:
                postfix_product[j]= postfix_product[j+1]*nums[j]

        # Adding to result list by taking the current element's previous and post elements values
        for k in range(len(nums)):
            if k == 0:
                res[k]= postfix_product[k+1]
            elif k== len(nums)-1:
                res[k]= prefix_product[k-1]
            else:
                res[k]=prefix_product[k-1]*postfix_product[k+1]
           
        return res

sol = Solution()
arr= [-1,1,0,-3,3]
print(sol.productExceptSelf(arr))
        