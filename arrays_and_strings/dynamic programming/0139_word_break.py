'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        # Convert the list into a set for faster lookups.
        wordSet = set(wordDict)

        # dp[i] means whether s[i:] can be segmented into valid dictionary words.
        dp = [False] * (len(s) + 1)

        # Base case: an empty suffix is always segmentable.
        dp[len(s)] = True

        # Work backwards so smaller suffixes are already solved.
        for i in range(len(s) - 1, -1, -1):
            # Try every word in the dictionary at the current position.
            for word in wordSet:
                # Make sure the word fits inside the string from index i.
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    # If the remaining suffix is valid, mark this position as valid.
                    if dp[i + len(word)]:
                        dp[i] = True
                        break

        # The answer for the whole string is stored at dp[0].
        return dp[0]


'''
Walkthrough Example

Input:
s = "leetcode"
wordDict = ["leet", "code"]

Step 1:
wordSet = {"leet", "code"}
dp = [False, False, False, False, False, False, False, False, False]
dp[8] = True

Step 2:
Start from the end of the string.

i = 4
Substring = "code"
It matches "code" in the set.
dp[4 + 4] = dp[8] is True
So dp[4] = True

Step 3:
i = 0
Substring = "leet"
It matches "leet" in the set.
dp[0 + 4] = dp[4] is True
So dp[0] = True

Final answer:
dp[0] = True

Time Complexity: O(n * m * k)
Space Complexity: O(n)

Where:
n = length of string s
m = number of words in wordDict
k = average length of a word
'''