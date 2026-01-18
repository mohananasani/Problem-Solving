"""
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.


Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Real world:
Statement:  Smallest contiguous window
            containing all required events.
Scenaro:    
    Log stream: "ERR123...AUTH_FAIL...USER42...TIMEOUT...DB_FAIL..."
    
    They want to find:

        The smallest log segment that contains
        "AUTH_FAIL", "DB_FAIL", "TIMEOUT"

"""

class Solution:
    """
        Time  : O(n)
        Space : O(k)
        Approach: Sliding Window + HashMap approach
        
    """
    def minWindow(self, s="ADOBECODEBANC", t="ABC"):
        target_string_total_chars= len(t)
        output_left, output_right = 0, float("inf")  # + infinity, float("-inf") for - infinity
        chars_found_in_source = 0
        fre_map = dict()
        for char in t:
            fre_map[char]= fre_map.get(char,0)+1
        start = 0
        # Starting the pointers from where acutal chars are present in both strings
        while start<len(s) and s[start] not in fre_map:
            start+=1
        if start == len(s):
            return ""
        left=right = start
        while right<len(s):
            # checking the current present in target string
            if s[right] in fre_map and fre_map.get(s[right]!=0):
                # Reducing the frequency count and updating chars to found count
                fre_map[right]= fre_map.get(s[right])-1
                chars_found_in_source+=1
            # If found all chars in source string 
            if target_string_total_chars == chars_found_in_source:
                # comparing the lengths and updating final output window pointers
                if right-left < output_right-output_left:
                    output_left,output_right = left, right

                # Increase it's count, because it is eliminating from window
                fre_map[left] = fre_map.get(s[left])+1
                # Increasing to chars to find count
                chars_found_in_source-=1
                # Finally moving to right side
                left+=1
                # Moving left pointer the index where the index char is in target string
                while s[left] not in fre_map:
                    left+=1
            right+=1
        return "" if output_right == float("inf") else s[output_left:output_right+1]    
                

# Modifed above logic into cleaner and industry standards
class Solution:
    """
        Time  : O(n)
        Space : O(k)
        Approach: Sliding Window + HashMap approach
        
    """
    def minWindow(self, s="ADOBECODEBANC", t="ABC"):
        

        # Edge case: if either string is empty
        if not t or not s:
            return ""

        # Build frequency map for target string `t`
        # Example: t = "AABC" -> {'A':2, 'B':1, 'C':1}
        freq = {}
        for c in t:
            freq[c] = freq.get(c, 0) + 1

        # Number of unique characters we need to match
        required = len(freq)

        # Count of characters currently satisfied in window
        formed = 0

        # Current window frequency
        window = {}

        # Left pointer
        l = 0

        # ---------------- TUPLE PACKING ----------------
        # Python packs multiple values into a tuple
        # ans = (window_length, left_index, right_index)
        #
        # Example:
        # ans = 10, 2, 5
        # ans -> (10, 2, 5)
        #
        # We use:
        # ans[0] -> minimum length
        # ans[1] -> left index
        # ans[2] -> right index
        #
        # Initialize length with +infinity
        # so first valid window is always smaller
        ans = float("inf"), None, None
        # -----------------------------------------------

        # Expand window using right pointer
        for r in range(len(s)):

            c = s[r]

            # Add current char to window map
            window[c] = window.get(c, 0) + 1

            # If char is required and exact frequency matched
            if c in freq and window[c] == freq[c]:
                formed += 1

            # Try to shrink window if valid
            while l <= r and formed == required:

                # Check if current window is smaller than previous best
                if r - l + 1 < ans[0]:
                    # Tuple packing again
                    # (length, left, right)
                    ans = (r - l + 1, l, r)

                # Remove left character from window
                window[s[l]] -= 1

                # If required char count breaks, window invalid
                if s[l] in freq and window[s[l]] < freq[s[l]]:
                    formed -= 1

                # Move left pointer
                l += 1

        # If no valid window found
        if ans[1] is None:
            return ""

        # Extract substring using stored indices
        return s[ans[1]:ans[2]+1]
