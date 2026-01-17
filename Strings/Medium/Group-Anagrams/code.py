"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""

class BrutForceSolution:
    """
    Time: O(n * n * k log k)
        n = for visting the main strings in first loop
        n = for finding it's anagrams in remanining strings
        k log k = for sorting the strings
    Space: O(n )
        Apart from result array, we are maintaining set for the elements we visited
        If there is no set, then it will O(1), generally ouput array doesn't count, as we need to return the output.

    """
    def groupAnagrams(self, strs=["eat","tea","tan","ate","nat","bat"]):
  
        visited = set()
        first = 0
        result = []

        while first < len(strs):

            if first in visited:
                first += 1
                continue

            anagrams = [strs[first]]
            second = first + 1

            while second < len(strs):

                if second in visited:
                    second += 1
                    continue

                if sorted(strs[first]) == sorted(strs[second]):
                    anagrams.append(strs[second])
                    visited.add(second)

                second += 1

            result.append(anagrams)
            visited.add(first)
            first += 1

        return result


class OptimalSolution:
    """
    Time: O(n * k log k)
        n = number of strings
        k = max length of a string
    Space: O(n )
        Dictionary stores all unique strings as keys.
        Output list → O(n)
    Approach:
        Used map 
            keys: sorted string -> if two are anagrams, then they are equal when we sort,
                So when we use sorted string as key, we will get same key for anagrams
            values: list of strings or words
    """
    
    def groupAnagrams(self, strs=["eat","tea","tan","ate","nat","bat"]):
  
        mp = {}
    
        for s in strs:
            # sorting O(k log k) where k is the max string length
            # joining O(k)
            # total O(k log k + k) = O(k log k)
            key = ''.join(sorted(s))  # key type string
            """
            sorted(s) -> list: list cannot be used for hashing, as list is mutable, so hash key changes when list changed
            String: strings can be used for hashing
            Tuple: Tuples also used for hashing, as it is immutable
            key = tuple(sorted(s)) we can also use tuple key like this
            """
    
            if key not in mp:
                mp[key] = []
    
            mp[key].append(s)
    
        return list(mp.values())

arr = ["eat","tea","tan","ate","nat","bat"]
sol = OptimalSolution()
res = sol.groupAnagrams(arr)
print(res)