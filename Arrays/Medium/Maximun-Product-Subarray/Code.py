class Solution:
    def maxProduct(self, nums):
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]

            """ 
            When the current value is negative, then least or min value can flip the product to large value because - * - = +
            EG: [-6, 3, -2]
            That's why we should track the min product as it has a significance value 
            and we should swap min, and max when we have -ve current value.
            """
            if curr < 0:
                max_prod, min_prod = min_prod, max_prod

            # Taking max value out of current value and product of it's previous values including current value
            max_prod = max(curr, curr * max_prod)  

            # Taking min value out of current value and product of it's previous values including current value
            min_prod = min(curr, curr * min_prod)

            result = max(result, max_prod)

        return result
    
"""
    Logic is simple
    -> Iterate through each element
    -> We will store max and min for the current element. 
    -> Max is for result, Min for negative numbers, as Min can turn negative number to high yield.
"""