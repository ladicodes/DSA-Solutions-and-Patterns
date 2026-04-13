"""15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

The solution set must not contain duplicate triplets.
"""


class Solution(object):
    def threeSum(self, nums):
        # Sort first so we can use two pointers and skip duplicates easily.
        nums.sort()
        result = []

        # Fix one number, then solve a 2Sum-like problem on the remaining range.
        for i in range(len(nums) - 2):
            # Skip duplicate fixed values to avoid duplicate triplets.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Move pointers past duplicates for both sides.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < 0:
                    # Need a larger sum, so move left pointer right.
                    left += 1
                else:
                    # Need a smaller sum, so move right pointer left.
                    right -= 1

        return result


"""
Step by Step Example

nums = [-1, 0, 1, 2, -1, -4]
After sorting: [-4, -1, -1, 0, 1, 2]

i = 0 (value = -4)
  left = 1, right = 5
  -4 + (-1) + 2 = -3 < 0 -> move left
  -4 + (-1) + 2 = -3 < 0 -> move left
  -4 + 0 + 2 = -2 < 0 -> move left
  -4 + 1 + 2 = -1 < 0 -> move left
  No triplet for i = 0

i = 1 (value = -1)
  left = 2, right = 5
  -1 + (-1) + 2 = 0 -> add [-1, -1, 2]
  move pointers inward
  left = 3, right = 4
  -1 + 0 + 1 = 0 -> add [-1, 0, 1]

i = 2 (value = -1)
  Duplicate fixed value of previous i, skip

Result: [[-1, -1, 2], [-1, 0, 1]]

Time Complexity: O(n^2)
Space Complexity: O(1) extra space (excluding output)
"""
