## Walkthrough Example

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
