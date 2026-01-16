class Solution1:
    """
    Time: O(n)
    Space: O(n)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_size = 0
        seen = set()
        for right in range(len(s)):
            # Removing and Shrinking the window 
            # While loop only runs when it is found that the current char is present in seen set
            # So removing the previous elements including the seen and making left pointer start after that
            while s[right] in seen:
                seen.remove(s[left])
                left+=1

            seen.add(s[right])
            curr_window_size = right-left+1
            max_size = max(max_size, curr_window_size)
        return max_size
    
class Solution2:
    """
    Time: O(n)
    Space: O(n)
    Desc: Solution1 left pointer is moving slowly by removing and then moving
          Current solution left pointer is directly moving based on last seen index
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_size = 0
        last_seen = dict()
        for right in range(len(s)):
            # Directly jumping instead of removing and moving one by one
            if s[right] in last_seen:
                """
                if we directly or blindly move left then if the seen index is below/left side of left pointer
                This time we are moving back 
                Ex: ABBA at 4th iteration we check A and last seen is 0 so  we will blindly move back to 0 index which is wrong
                """
            #   left = last_seen[s[right]]+1 
                """
                Preventing backward pointer moving by taking max of positions
                """
                left = max(last_seen[s[right]]+1, left)

            # Storing and overriding last seen index of elements
            last_seen[s[right]]= right
            curr_window_size = right-left+1
            max_size = max(max_size, curr_window_size)
        return max_size
            


arr = [-1,0,1,2,-1,-4]
sol = Solution1()
print(sol.threeSum(arr))
