"""
435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104

Note: 
✅ Valid Intervals

These are allowed:

1️⃣ Independent (no contact)
[1,2] and [4,5]


✔ No overlap

2️⃣ Touching at exactly one point
[1,2] and [2,3]


✔ Still valid
(because problem explicitly allows this)

❌ Invalid Intervals

Only this is invalid:

3️⃣ Actual overlap
[1,3] and [2,4]

Statement:

Used in railway scheduling systems where only one train can use a track at a time.
Train slots are submitted by different stations and control centers.
We need to cancel the minimum number of conflicting train schedules
to ensure no two trains use the same track at the same time.

Scenario

A railway network has a single track section between two major stations.
Train timings are booked by different regional offices.

Because schedules come from multiple systems:
• They are unordered
• Some train timings overlap

The railway authority must:

Remove the minimum number of conflicting trains
so the remaining schedule is non-overlapping and safe.

"""

class Solution:
    """
        Time  : O(n * logn)
        Space : O(1)
        Approach: None
        Steps:
            Sort first
            Traverse through each element
            Maintain prev end to compare with each element start value while traversing
            If current is less than not = to prev end, then it is a conflict.
            So increase the count of invalid intervals.
    """
    def eraseOverlapIntervals(self, intervals):
        # Sort intervals by their end time (greedy strategy)
        intervals.sort(key=lambda x: x[1])

        # Counter for intervals to remove
        count = 0

        # Track the end time of last accepted interval
        prev_end = intervals[0][1]

        # Traverse the rest of intervals
        for i in range(1, len(intervals)):

            # If current interval overlaps with previous
            if intervals[i][0] < prev_end:
                # Increment removal count
                count += 1
            else:
                # Update previous end to current interval's end
                prev_end = intervals[i][1]

        # Return number of intervals removed
        return count