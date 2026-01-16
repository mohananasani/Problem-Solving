class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<2:
            return []
        left, right = 0, len(nums)-1
        map= dict()
        for i in range(0, len(nums)):
            curr_ele = nums[i]
            second_ele = target-nums[i]
            if second_ele in map and map[second_ele] !=i:
                return [i, map[second_ele]]
            else:
                # Add to map for further checks
                map[curr_ele] = i
        return []