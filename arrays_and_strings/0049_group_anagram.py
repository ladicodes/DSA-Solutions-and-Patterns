'''
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
'''
from collections import defaultdict  # import defaultdict to automatically create empty lists

class Solution:
    def groupAnagrams(self, word: List[str]) -> List[List[str]]:
        answer = defaultdict(list)  # create a dictionary where each key maps to a list automatically

        for s in word:  # loop through each word in the input list
            key = "".join(sorted(s))  # sort the characters of the word to create a common key for anagrams
            answer[key].append(s)  # add the original word to the list corresponding to this key

        return list(answer.values())  # return all grouped anagrams as a list of lists

'''
Walkthrough Example
Input:
word = ["eat", "tea", "tan", "ate", "nat", "bat"]
Step 1: Initialize
answer = {}

(defaultdict will auto-create lists)

Step 2: Loop through words
s = "eat"
sorted("eat") → "aet"
answer = {
    "aet": ["eat"]
}
s = "tea"
sorted("tea") → "aet"
answer = {
    "aet": ["eat", "tea"]
}
s = "tan"
sorted("tan") → "ant"
answer = {
    "aet": ["eat", "tea"],
    "ant": ["tan"]
}
s = "ate"
sorted("ate") → "aet"
answer = {
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan"]
}
s = "nat"
sorted("nat") → "ant"
answer = {
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"]
}
s = "bat"
sorted("bat") → "abt"
answer = {
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
}
Step 3: Return result
list(answer.values())
[
 ["eat", "tea", "ate"],
 ["tan", "nat"],
 ["bat"]
]
Time Complexity: O(n * k log k)
- n = number of words
- k = length of each word (sorting each word)

Space Complexity: O(n * k)
- storing all words in hashmap
'''