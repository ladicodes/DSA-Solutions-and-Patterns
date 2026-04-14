'''
164. Maximum Gap

Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

 

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
'''
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()  # sort the array so consecutive elements make sense

        if len(nums) < 2:
            return 0  # if less than 2 elements, no gap exists

        max_diff = 0  # this will store the largest gap found

        for i in range(len(nums) - 1):  # loop through all consecutive pairs
            num = nums[i+1] - nums[i]  # calculate difference between current and next number
            max_diff = max(max_diff, num)  # update max_diff if this gap is bigger

        return max_diff  # return the largest gap found
    
'''
Walkthrough Example
Input:
nums = [3,6,9,1]
Step 1: Sort
[1,3,6,9]
Step 2: Initialize
max_diff = 0
Step 3: Loop through pairs
i = 0
nums[1] - nums[0] = 3 - 1 = 2
max_diff = max(0, 2) = 2
i = 1
nums[2] - nums[1] = 6 - 3 = 3
max_diff = max(2, 3) = 3
i = 2
nums[3] - nums[2] = 9 - 6 = 3
max_diff = max(3, 3) = 3
Final Answer:
3
 Key Understanding

Sorting makes sure:

nums[i] and nums[i+1]

are the closest neighbors in order

So their difference is meaningful.

Complexity
Time Complexity: O(n log n)  
Space Complexity: O(1)     
'''