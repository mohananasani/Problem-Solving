class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<2:
            return []
        left, right = 0, len(nums)-1
        map= dict()
        for cur_ind in range(0,len(nums)):
            map[nums[cur_ind]]= cur_ind
        for i in range(0, len(nums)):
            first_ele = nums[i]
            second_ele = target-nums[i]
            if second_ele in map and map[second_ele] !=i:
                return [i, map[second_ele]]
        return []