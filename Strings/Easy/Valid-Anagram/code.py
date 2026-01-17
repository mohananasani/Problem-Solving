"""
242. Valid Anagram

If string is anagram when all character are used only once in second string in different order and lenth is same 
then second string will be called as anagram of first string.

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Real world Example




"""
class BrutForce:
    """
    Time: O(n log n) + O(n log n) = O(n log n)
    Space: O(n) + O(n) = O(n)

    """
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        s=sorted(s)
        t=sorted(t)

        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True

class BrutForce2:
    """
    Time: O(n*n)
    Space: O(n) Storing indexes in set

    """
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        index_set = set()

        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j] and j not in index_set:
                    index_set.add(j)
                    break

        return len(index_set) == len(s)
       


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

