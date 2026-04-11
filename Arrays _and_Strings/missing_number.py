"""268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return
the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
8 is the missing number in the range since it does not appear in nums.
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Initialize a variable to store the sum of numbers in the array.
        total_nums = 0

        # Initialize a variable to store the sum of numbers from 0 to n.
        total_number = 0

        # Loop through all numbers from 0 to n (inclusive).
        for i in range(0, len(nums) + 1):
            # Add each number in the full range to get the expected total sum.
            total_number += i

        # Loop through all numbers in the given array.
        for j in nums:
            # Add each number in the array to get the actual sum.
            total_nums += j

        # Return the difference between expected sum and actual sum (the missing number).
        return total_number - total_nums


"""
Walkthrough Example
nums = [3, 0, 1]
Step 1:
len(nums) = 3

 Range should be:

0, 1, 2, 3
Step 2: First Loop (Expected Sum)
total_number = 0

i = 0 → total = 0
i = 1 → total = 1
i = 2 → total = 3
i = 3 → total = 6

 Expected sum = 6

Step 3: Second Loop (Actual Sum)
total_nums = 0

j = 3 → total = 3
j = 0 → total = 3
j = 1 → total = 4

 Actual sum = 4

Step 4: Final Answer
6 - 4 = 2

Missing number = 2
Time Complexity: O(n)
Space Complexity: O(1)
"""
