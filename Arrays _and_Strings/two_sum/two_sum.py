"""Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.
"""


class Solution(object):
    def twoSum(self, nums, target):
        # Create a dictionary to store numbers and their indices.
        map = {}

        # Loop through the list using index.
        for i in range(len(nums)):
            # Get the current number.
            num = nums[i]

            # Calculate the number needed to reach the target.
            diff = target - num

            # Check if we have already seen the needed number.
            if diff in map:
                # If yes, return the index of the previous number and current index.
                return [map[diff], i]

            # Store the current number and its index for future checks.
            map[num] = i


"""
Step by Step Example

nums = [2, 7, 11, 15]
target = 9

Step 1:
i = 0
num = 2
diff = 9 - 2 = 7

Have we seen 7? No
Store: {2: 0}

Step 2:
i = 1
num = 7
diff = 9 - 7 = 2

Have we seen 2? Yes
Return: [0, 1]

Time Complexity: O(n)
Space Complexity: O(n)
"""
