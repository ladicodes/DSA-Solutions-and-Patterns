# THE PROBLEM

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


# LINK : https://leetcode.com/problems/first-missing-positive/


# PATTERN

Array

# INTUITION

The problem asks to return the smallest positive integer that is not present in the input list

Because the input list is unordered, the first step i took was to sort the list using python's built-in method sort()

And since the lowest positive integer is 1, I set the least variable to 1.

A for loop was used to linearly scan through the list looking for a positive integer. Any negative integer encountered skipped.

Once a positive integer is found, if the integer is equal to out least value then least is incremented and the loop goes to the next index

But if least value is less than the current integer, we have found out lowest positive integer

# APPROACH

Example 1:

Input: nums = [1,2,0]
Output: 3

Explanation: The algorithm first sort the list to get [0, 1, 2]. And a for loop scans through this list from 0, since 0 is not exactly a positive integer, it is skipped. 

The next value is 1 which is a positive integer. Since 1 is in our list, the lowest positive integer that is not in the list is no longer 1, so the "least" variable is incremented hoping that 2 would be the lowest positive integer not in the list

The next value is 2 which is a positive integer. Since 2 is also in out "least", the lowest positive integer that is not in the list cannot be 2, the "least" variable is incremented again.

2 is the end of the list and so 3 would be the lowest positive integer not in the list which is the value of "least"


# COMPLEXITY
Time complexity: Best case: O(1)
                 Worst case: O(n)
Space complexity: Best case: O(1)
                  Worst case: O(n)
