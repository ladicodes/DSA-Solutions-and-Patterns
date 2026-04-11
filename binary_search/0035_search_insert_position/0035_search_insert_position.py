"""
Problem Name: Search Insert Position

Link: https://leetcode.com/problems/search-insert-position/

Pattern: Binary Seacrch

This is a standard binary search problem with the only caveat is that we're returning the index of where a value will be if it were in the array. It's the same standard binary search algorithm except at the end of the while loop we return the left pointer.
The reason being that the algorithm searches for a target within the bounds of [left, right] with mid = (left + right // 2). If the number is target >= nums[mid], then we know the target cannot be in any of the indexes <= left so we increment left by 1 (left + 1). Likewise if the target <= nums[mid], then we know that the number can't be in any of the indexes >= right so we decrement right by 1 (right + 1).
Now look at the condition of the while loop being left <= right. When it is not met, it means that the target cannot be below the left index as it as increased to the point where it is the same value as the right pointer and it cannot also be the right pointer as that index would have been checked already.
This leaves us with one last option, the target position is at left + 1 as the nums[right] would have been checked already but the target can't be at any position less than left as well.

Time Complexity: O(logn)
Space Complexity: O(1)

"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            elif target == nums[mid]:
                return mid

        return left
