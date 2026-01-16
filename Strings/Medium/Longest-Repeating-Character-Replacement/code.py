"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.


Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

Real world Example

Find the longest continuous production streak
where you can excuse up to k bad days


"""
class BrutForce:
    """
    Time: O(n*n)
    Space: O(1)

    """
    def characterReplacement(self, s, k):
        if len(s)== 0:
            return 0
        if len(s)==1:
            return 1
        max_size = 1
        # Checking longest possible from each element
        for left in range(len(s)):
            print(f"iteration {left}")
            right = left+1
            replaced = 0
            
            seen = set(s[left])
            while right<len(s) and replaced<=k:
                # Assuming replaced by incrementing flag
                if s[right] not in seen:
                    replaced+=1
                max_size = max(max_size, right+1-left)
                right+=1
            print("max_size", max_size)
        return max_size


class OptimalSolution:
    """
    Time: O(n*m) 
    Space: O(m)
        Where m is the unique chars possible to pass as input string
    
    Time complexity:
        n for visiting each char * m for time taking to fetch most frequent chars out of unique chars in input array
        If we wil get only same case alphabets, then unique or distinct chars will be A-A ie 26, then
        O(n*26) ~ O(n) where 26 is consider as constant

    Space complexity:
        We are storing the each unique char frequency.If we pass only upper or lowercase alphabets then it will become O(26) and it will considered as constant
        then O(1) space
    """
    def characterReplacement(self, s, k):
        left, right = 0, 0
        curr_window_char_frequency = dict()
        max_length = 0
        while right<len(s):
            if s[right] not in curr_window_char_frequency:
                curr_window_char_frequency[s[right]]=1
            else:
                curr_window_char_frequency[s[right]]+=1
            
            # Getting most occured char value of the current window
            most_frequent_value = 0
            for key, value in curr_window_char_frequency.items():
                most_frequent_value = max(most_frequent_value, value)

            no_of_chars_to_replace = (right+1-left)-most_frequent_value # (right+1-left) gives current window length
            valid_window = no_of_chars_to_replace<= k

            # More chars to replace
            if not valid_window:
                # Reducing left pointer char frequency
                curr_window_char_frequency[s[left]]-=1
                left+=1

            curr_window_lenght = right+1-left

            # Updating max size window length
            max_length = max(max_length,curr_window_lenght)

            right+=1
        return max_length


# Line of Code optimization of above one
# Reduced O(26) extra time for getting max frequency
class OptimalSolution1:
    """
    Time: O(n) 
    Space: O(m) => O(26) => O(1)
    """
    def characterReplacement(self, s, k) -> int:
        left = 0
        freq = {}
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])

            """
            Checking the window is valid or not if not valid
            Removing the left pointer frequency
            Moving left pointer to rightward direction
            """
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

