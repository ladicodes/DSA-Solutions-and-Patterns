## Walkthrough Example

Input:
nums = [2, -1, 1]
Step 1:
closest_num = 2
Step 2 (Loop):
num = 2 → abs(2) = 2 → no change
num = -1 → abs(-1) = 1 < 2 → update → closest_num = -1
num = 1 → abs(1) = 1 == abs(-1) → no update here
Step 3 (Final Check):
closest_num = -1
It is negative
Its positive version 1 is in nums

So return:

1
Complexity
Time Complexity: O(n)
Space Complexity: O(1)
