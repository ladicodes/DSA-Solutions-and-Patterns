'''
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitting = s.split() # split the words to individual word
        return len(splitting[-1]) #get the last element of the splitted word
'''
walkthorugh example
s = "Hello word"
s.split turns it to ["hello", "world"]
so to the get length of last element, use len(splitting[-1])
time and space complexity is o(n)
'''
        