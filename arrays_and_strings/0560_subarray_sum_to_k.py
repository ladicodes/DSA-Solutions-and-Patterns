'''
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
'''
class Solution:  # Define the solution class
    def subarraySum(self, nums, k):  # Function to count subarrays with sum k
        count = 0  # This will store the total number of valid subarrays found
        current_sum = 0  # This keeps track of the running sum as we move through the array
        prefix_sum = {0: 1}  # Dictionary to store prefix sums and their frequency (0 is seen once initially)

        for num in nums:  # Loop through each number in the array
            current_sum += num  # Add current number to running sum

            if (current_sum - k) in prefix_sum:  # Check if there exists a previous sum that makes subarray sum = k
                count += prefix_sum[current_sum - k]  # Add how many times that previous sum occurred

            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1  # Store/update current sum frequency

        return count  # Return total number of subarrays with sum k

'''
Walkthrough Example (Follow this carefully)
Input:
nums = [1, 2, 3]
k = 3
Step-by-step Execution
Start:
current_sum = 0
count = 0
prefix_sum = {0:1}
Step 1: num = 1
current_sum = 1

Check:

current_sum - k = 1 - 3 = -2  → not in prefix_sum

So:

No subarray found yet

Update:

prefix_sum = {0:1, 1:1}
Step 2: num = 2
current_sum = 3

Check:

current_sum - k = 3 - 3 = 0  → FOUND

 prefix_sum[0] = 1

So:

count = 1

Meaning:

[1,2] → sum = 3

Update:

prefix_sum = {0:1, 1:1, 3:1}
Step 3: num = 3
current_sum = 6

Check:

current_sum - k = 6 - 3 = 3 → FOUND

 prefix_sum[3] = 1

So:

count = 2

Meaning:

[3] → sum = 3

Update:

prefix_sum = {0:1, 1:1, 3:1, 6:1}
Final Answer:
2
'''