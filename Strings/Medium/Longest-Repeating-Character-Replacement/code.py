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

Real World Application:

Find the longest continuous production streak
where you can excuse up to k bad days


"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
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
            no_of_chars_to_replace = (right+1-left)-most_frequent_value
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
    

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])

            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

