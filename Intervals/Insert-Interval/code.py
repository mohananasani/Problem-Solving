"""
57. Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105

Real world:
Statement:  This is used in scheduling systems like calendars and booking platforms where time slots must remain sorted 
            and non-overlapping while inserting new reservations.
Scenario:    
    A hospital system stores booked appointments as non-overlapping time slots:
    [[9:00, 9:30], [10:00, 10:30], [11:00, 11:45]]

    Now a patient wants to book:
    [9:20, 10:15]
    
    # converting into minutes
    appointments = [[540,570], [600,630], [660,705]]
    new_booking = [560,615]

    output
    [[540,615], [660,705]]

    Doctor is now busy continuously from 9:00 → 10:15

"""

class Solution:
    """
        Time  : O(n)
        Space : O(1) -> As we need to return the output
        Approach: None
        Steps:
            Add all intervals that end before newInterval starts
            Merge all overlapping intervals
            Add the rest
    """
    def insert(self, intervals, newInterval):
        result = []
        # ready to insert
        to_insert = newInterval
        low, high = 0,1
        for cur_int in intervals:

            # Nothing to compare or insert
            if to_insert is None:
                result.append(cur_int)
            # Have element to compare
            else:

                # conflict
                if cur_int[low]<=to_insert[low]<=cur_int[high] or cur_int[low]<=to_insert[high]<=cur_int[high]:

                    to_insert[low] = min(to_insert[low], cur_int[low])
                    to_insert[high] = max(to_insert[high], cur_int[high])

                # if to insert is less than current
                elif to_insert[high] < cur_int[low]:
                    # insert to insert first
                    result.append(to_insert)
                    to_insert = None
                    result.append(cur_int)
                # if current is within to insert range eg current = [4,6] and to insert = [3,7]
                elif to_insert[low]<cur_int[low] and to_insert[high] > cur_int[high]:
                    continue
                # to insert is ahead with current
                else:
                    result.append(cur_int)
        # At last if we have something to insert
        if to_insert is not None:
            result.append(to_insert)
        return result

# Modifed above logic into cleaner and industry standards but anything is fine
class Solution:
    """
        Time  : O(n)
        Space : O(1) -> As we need to return the output
        Approach: None
        Steps:
            Add all intervals that end before newInterval starts
            Merge all overlapping intervals
            Add the rest
    """
    def insert(self, intervals, newInterval):
        res = []
        i = 0
        n = len(intervals)

        # 1) Add intervals BEFORE newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2) Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add merged interval
        res.append(newInterval)

        # 3) Add remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
