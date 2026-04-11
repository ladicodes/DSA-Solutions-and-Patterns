'''
Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)                 # get total sum of the entire array so we can derive right side in O(1)
        left = 0                           # initialize running sum of elements to the left of current index

        for i in range(len(nums)):         # iterate through each index to test it as a potential pivot
            right = total - left - nums[i] # compute right sum using total minus left sum minus current element
            if right == left:              # check if left and right sums are equal at this index
                return i                   # if equal, this is the pivot index, so return it
            left += nums[i]                # add current element to left sum before moving to next index

        return -1                          # if no pivot index is found, return -1
'''
Walkthrough Example
Input:
nums = [1, 7, 3, 6, 5, 6]
Step 1: Compute total
total = 1 + 7 + 3 + 6 + 5 + 6 = 28
left = 0
Step-by-step iteration:
i = 0
nums[0] = 1
left = 0
right = 28 - 0 - 1 = 27

left ≠ right → move on
Update:

left = 0 + 1 = 1
i = 1
nums[1] = 7
left = 1
right = 28 - 1 - 7 = 20

left ≠ right
Update:

left = 1 + 7 = 8
i = 2
nums[2] = 3
left = 8
right = 28 - 8 - 3 = 17

left ≠ right
Update:

left = 8 + 3 = 11
i = 3
nums[3] = 6
left = 11
right = 28 - 11 - 6 = 11

left == right → return index

Output = 3
Time Complexity
Computing total sum: O(n)
Loop through array once: O(n)

Total time complexity:

O(n)
Space Complexity
Only using a few variables (total, left, i)
O(1)
'''