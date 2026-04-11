"""Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanatio
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Start pointer at the beginning of the array
        left = 0

        # Start pointer at the end of the array
        right = len(numbers) - 1

        # Keep checking pairs until pointers meet
        while left < right:
            # Calculate the sum of the two current elements
            current_sum = numbers[left] + numbers[right]

            # Check if we found the required pair
            if current_sum == target:
                # Return positions (1-based index as required)
                return [left + 1, right + 1]

            # If sum is too small
            elif current_sum < target:
                # Move left pointer right to increase the sum
                left += 1
            else:
                # if sum is too big
                # Move right pointer left to decrease the sum
                right -= 1

        # Return default if no pair is found (safety)
        return [-1, -1]


"""
Walkthrough Example
Input:
numbers = [2,7,11,15]
target = 9
Step 1:
left = 0 (2)
right = 3 (15)
2 + 15 = 17 > 9

 Too big → move right

right = 2
Step 2:
left = 0 (2)
right = 2 (11)
2 + 11 = 13 > 9

 Too big → move right

right = 1
Step 3:
left = 0 (2)
right = 1 (7)
2 + 7 = 9 

 Found answer

return [1, 2]
🔹 Time and Space Complexity
⏱ Time Complexity:

 O(n)

Each pointer moves at most once across the array
 Space Complexity:

 O(1)

No extra space used (only variables)
"""
