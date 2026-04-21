'''

Code
Testcase
Test Result
Test Result
347. Top K Frequent Elements
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

 
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}  # dictionary to store how many times each number appears

        freq = [[] for i in range(len(nums) + 1)]  
        # create a list of empty lists where index = frequency
        # index 0 → numbers that appear 0 times (unused)
        # index 1 → numbers that appear once
        # index 2 → numbers that appear twice
        # ...
        # up to len(nums)

        for i in nums:
            count[i] = 1 + count.get(i, 0)  
            # count frequency of each number
            # if number not seen before → start from 0, then add 1

        for n, c in count.items():
            freq[c].append(n)  
            # place each number into the bucket that matches its frequency
            # example: if number appears 3 times → go to freq[3]

        res = []  # this will store the top k frequent elements

        for i in range(len(freq) - 1, 0, -1):  
            # loop from highest frequency to lowest
            # we want most frequent numbers first

            for n in freq[i]:
                res.append(n)  
                # add number from this frequency bucket into result

                if len(res) == k:
                    return res  
                    # once we have k elements, return immediately
'''
Walkthrough Example
Input:
nums = [1,1,1,2,2,3]
k = 2
Step 1: Count frequencies
count = {
    1: 3,
    2: 2,
    3: 1
}
Step 2: Create buckets
freq = [
 [],        # index 0 (unused)
 [3],       # numbers appearing once
 [2],       # numbers appearing twice
 [1],       # numbers appearing three times
 [], [], ...
]
Step 3: Traverse from back

Start from highest frequency:

i = 3
freq[3] = [1]
res = [1]
i = 2
freq[2] = [2]
res = [1, 2]

Now:

len(res) == k → 2
Output:
[1, 2]

Time Complexity: O(n)
- counting → O(n)
- filling buckets → O(n)
- scanning buckets → O(n)

Space Complexity: O(n)
- hashmap + buckets
'''