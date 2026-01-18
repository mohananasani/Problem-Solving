"""
5. Longest Palindromic Substring
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters

Real World Application:

Finding the longest symmetric DNA pattern


"""

class Solution1:
    """
    Time: O(n^2)
    Space: O(1)
    Approach:
        Visiting each center
        Expanding left and right from the center
    """

    def longPalindrome(self, s, left, right):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return left+1, right-1

    def longestPalindrome(self, s):
        start, end = 0, 0
        max_length = 0
        for center in range(len(s)):
            # Checking for even length palindrome eg "abbc". "bb" is also palindrome
            even_left, even_right = self.longPalindrome( s, left=center, right = center+1)
            # Checking for odd length palindrome eg "abcbd". "bcb" is palindrome
            odd_left, odd_right = self.longPalindrome(s, left=center, right=center)

            even_palindrome_len = even_right-even_left+1
            odd_palindrome_len = odd_right-odd_left+1
            if even_palindrome_len> max_length:
                max_length = even_palindrome_len
                start, end = even_left, even_right
            if odd_palindrome_len>max_length:
                max_length = odd_palindrome_len
                start, end = odd_left, odd_right
        return s[start:end+1]
    
# Same logic as above but removed unnecessary code
class Solution2:
    """
    Time: O(n^2)
    Space: O(1)
    Approach:
        Visiting each center
        Expanding left and right from the center
    """
    def longPalindrome(self, s, left, right):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return left+1, right-1

    def longestPalindrome(self, s: str) -> str:
        start = end = 0

        for i in range(len(s)):

            l1, r1 = self.longPalindrome(s, i, i)     # odd
            l2, r2 = self.longPalindrome(s, i, i+1)   # even

            if r1-l1 > end-start:
                start, end = l1, r1

            if r2-l2 > end-start:
                start, end = l2, r2

        return s[start:end+1]
    
string= "bacae"
sol = Solution2()
res = sol.longestPalindrome(string)
print(res)

