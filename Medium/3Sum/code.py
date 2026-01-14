class Solution:
    def threeSum(self, nums):
        res = set()
        nums.sort()

        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                
                if s == 0:
                    res.add((nums[i], nums[j], nums[k])) # Already sorted so no need to sort again
                    j += 1
                    k -= 1
                    
                elif s < 0:
                    j += 1
                else:
                    k -= 1
                    
        return [list(triplet) for triplet in res]


arr = [-1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(arr))
