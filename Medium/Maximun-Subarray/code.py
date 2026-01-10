class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = 0
        negative_count = 0
        is_all_negatives = False
        
        for num in nums:
            if num<0:
                negative_count+=1
        if negative_count== len(nums):
            is_all_negatives= True

        # If all nums are negative, then we should not combine, as it decreases value
        if is_all_negatives:
            for i in range(len(nums)):
                current_sum = nums[i]
                if current_sum>max_sum:
                    max_sum = current_sum

        else:
            for i in range(len(nums)):
                current_sum+=nums[i]
                # Resetting to 0 if we have negative sum, as it don't contributes to max sum
                if current_sum<0:
                    current_sum=0
                    continue
                # Updating max value
                if current_sum>max_sum:
                    max_sum = current_sum
        return max_sum
