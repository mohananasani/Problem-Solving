"""
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


"""
class BrutForceSolution:
    """
    Time: O(n^3)
        For generating all subsets take O(n^2)
        For checking generated is palindrome or not takes O(n)
    Space: O(1)

    Approach:
        Generating all subsets and checking whether that is palindrom or not
    """
    def checkPalindrom(self, s):
        start, end = 0, len(s)-1
        while start<=end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True
    
    def countSubstrings(self, s):
        sub_sets_count = 0
        # Generating all substrings
        for i in range(len(s)):
            for j in range(i, len(s)):
                curr_string = s[i:j+1]
                is_palindrome = self.checkPalindrom(curr_string)
                if is_palindrome:
                    sub_sets_count+=1
       
        return sub_sets_count
    
class OptimalSolution:
    """
    Time: O(n^2)
        Visiting each element takes n
        Checking palindrome takes n
    Space: O(1)
    Approach:
        Expand around center
    """
    def palindromesCount(self, s, left, right):
        count = 0
        while left>=0 and right<len(s) and s[left]==s[right]:
            # we are maintaining count of every palindromic substring when expanding around the center
            count+=1
            left-=1
            right+=1
        return count
    
    def countSubstrings(self, s):
        total = 0
        for center_index in range(len(s)):
            # odd palindromes count
            left_count = self.palindromesCount(s, center_index, center_index)

            # even palindromes count
            right_count = self.palindromesCount(s, center_index, center_index+1)

            total = total+left_count+right_count
        return total

            
string = "aaa"
sol = OptimalSolution()
res = sol.countSubstrings(string)
print("answer", res)
    
