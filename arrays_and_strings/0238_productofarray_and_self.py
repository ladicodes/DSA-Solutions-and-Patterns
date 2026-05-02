'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # number of elements
        n = len(nums)
        # answer[i] will hold product of all elements except nums[i]
        answer = [0] * n

        # left holds the running product of all elements to the left of i
        left = 1
        for i in range(n):
            answer[i] = left  # product of elements strictly left of i
            left *= nums[i]   # incorporate nums[i] for next index

        # right holds running product of elements to the right of i
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right  # multiply by product of elements to the right
            right *= nums[i]    # incorporate nums[i] for next left index

        return answer

# Walkthrough Example:
# nums = [1,2,3,4]
# After left pass: answer = [1,1,2,6] (products of prefixes before each index)
# After right pass: multiply by suffix products -> [24,12,8,6]

# Time Complexity: O(n) — two linear passes.
# Space Complexity: O(1) extra space (output array excluded per problem constraints).
