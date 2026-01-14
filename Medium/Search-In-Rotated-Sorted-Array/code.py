class Solution:
    def search(self, nums, target) -> int:
        start, end = 0, len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            # Checking the right part is sorted
            if nums[mid]<=nums[end]:
                # And if sorted checking target is in between right part
                if nums[mid]<target<=nums[end]:
                    # Moving the start to second part
                    start = mid+1
                else:
                    # Eventhough it is sorted and target is not present,then moving to left part
                    end = mid -1
            # If right is not sorted then left will be in sorted 
            else:
                # Checking whether the value is in between sorted part
                if nums[start]<=target<nums[mid]:
                    # Moving to start to  part
                    end = mid-1
                else:
                    # Eventhough it is sorted and target is not present,then moving to right part
                    start = mid +1
        return -1
        
        