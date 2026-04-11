"""2239. Find Closest Number to Zero

Given an integer array nums of size n, return the number with the value
closest to 0 in nums. If there are multiple answers, return the number with
the largest value.

Example 1:
Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.

Example 2:
Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
"""

from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # Assume the first number is the closest to zero.
        closest_num = nums[0]

        # Loop through each number in the array.
        for num in nums:
            # Check if the current number is closer to zero than the current closest.
            if abs(num) < abs(closest_num):
                # Update the closest number if a better one is found.
                closest_num = num

        # If the closest number is negative and its positive version also exists in the array.
        if closest_num < 0 and abs(closest_num) in nums:
            # return the positive version(since it is larger)
            return abs(closest_num)
        else:
            # Otherwise, return the closest number found.
            return closest_num

