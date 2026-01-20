"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

Statement:
    Used in scheduling systems where multiple bookings come from different sources and may overlap or be unordered.
    We need to merge overlapping appointments to know actual busy time.

Scenario
    A hospital system receives booked appointments from multiple departments.
    Because they come from different systems, they are unordered and may overlap.

"""

class Solution:
    """
        Time  : O(n * logn)
        Space : O(1) -> As we need to return the output
        Approach: None
        Steps:
            Sort first
            Traverse through each element
            Maintain compare element to compare with each element while traversing
            No confict with compare ele and curr element, add compare to result and push cur ele to compare
            At last add compare ele to res
    """
    def merge(self, intervals):
        res = []
        if len(intervals)<=1:
            return intervals
        """
        We need to sort in order to get in sequence otherwise it will be a mess
        EG: [[2,3],[5,5],[2,2],[3,4],[3,4]]
        After sorting 
        [[2, 3], [2, 2], [3, 4], [3, 4], [5, 5]]

        """
        intervals.sort(key=lambda x: x[0])

        to_compare = intervals[0]
        low, high = 0,1
        
        for i in range(1, len(intervals)):
            current = intervals[i]

            # Conflict - if any value falls in another
            if current[low]<=to_compare[low]<=current[high] or current[low]<=to_compare[high]<=current[high] or to_compare[low]<=current[low]<=to_compare[high] or to_compare[low]<=current[high]<=to_compare[high]:
                to_compare[low] = min(current[low],to_compare[low])
                to_compare[high] = max(current[high],to_compare[high])
            

            # if not conflict
            else:
                res.append(to_compare)
                to_compare = current

        # Finally adding the last one
        res.append(to_compare)

        return res

