'''
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
'''

class Solution:  # Define a class for the solution
    def findMaxAverage(self, nums: List[int], k: int) -> float:  # Function to find max average subarray of size k
        windows_sum = 0  # Store the sum of the current window
        max_average = 0  # Store the maximum average found so far
        
        for i in range(k):  # Build the first window of size k
            windows_sum += nums[i]  # Add each element to the window sum
            windows_average = windows_sum / k  # Calculate average of current window
        
        max_average = windows_average  # Initialize max average with first window
        
        for i in range(k, len(nums)):  # Slide the window across the array
            windows_sum = windows_sum - nums[i-k] + nums[i]  # Remove left element and add new right element
            windows_average = windows_sum / k  # Calculate new window average
            max_average = max(windows_average, max_average)  # Update max average if current is larger
        
        return max_average  # Return the maximum average found
    '''
Walkthrough Example
Input:
nums = [1,12,-5,-6,50,3]
k = 4
Step 1: First Window
[1, 12, -5, -6]
sum = 2
average = 0.5
max_average = 0.5
Step 2: Slide Window
Remove 1, add 50
new sum = 2 - 1 + 50 = 51
average = 12.75
max_average = 12.75
Step 3: Slide Again
Remove 12, add 3
new sum = 51 - 12 + 3 = 42
average = 10.5
max_average stays = 12.75
Final Answer:
12.75
Time Complexity: O(n)
Space Complexity: O(1)
'''