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

    Approach:
        comparing index sets lengths of two strings

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
    Time: O(n)
    Space: O(n) Storing each char frequency

    Approach: 
        Frequency increment and decrement

    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        # Storing each char frequency
        for char in s:
            count[char] = count.get(char, 0) + 1
        # Checking second string chars with frequency
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        return True
#If inputs strings are only small case alphabets

class OptimalSolution:
    """
    Time: O(n)
    Space: O(n) Storing each char frequency

    Approach: 
        Frequency increment and decrement

    """
    def isAnagram(a, b):
        if len(a) != len(b):
            return False
        # 26 containers for 26 alphabets and storing their frequencies
        freq = [0]*26
        # Character frequency increment
        for c in a:
            freq[ord(c)-97] += 1
        # Character frequence decrement
        for c in b:
            freq[ord(c)-97] -= 1
        
        # if we came to initial state where all char frequencies become 0, then two strings anagrams
        return all(x == 0 for x in freq)



    

