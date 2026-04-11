# Problem: 268. Missing Number

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

**Example 1:**
> **Input:** `nums = [3,0,1]`
> **Output:** `2`
> **Explanation:** `n = 3` since there are 3 numbers, so all numbers are in the range `[0,3]`. 2 is the missing number in the range since it does not appear in `nums`.

**Example 2:**
> **Input:** `nums = [0,1]`
> **Output:** `2`
> **Explanation:** `n = 2` since there are 2 numbers, so all numbers are in the range `[0,2]`. 2 is the missing number in the range since it does not appear in `nums`.

## Link
https://leetcode.com/problems/missing-number/

## Pattern
Math (Gauss's Formula)

## Key Improvement
Use of Gauss's Formula for Sum in an Arithmetic Progression rather than iterating

## Intuition
The problem states that the array contains `n` unique numbers in the range `[0, n]`. This means the length of the array itself is `n`. If no number was missing, the array would contain every integer from `0` to `n`. 

Instead of iterating with multiple loops to find the expected sum, we can use simple math. We calculate what the sum of all numbers from `0` to `n` *should* be using Gauss's formula for an arithmetic sequence. The difference between this expected sum and the actual sum of our array is exactly the missing number.

## Approach (Step by Step)
1. **Find `n`:** Get the length of the given `nums` array.
2. **Calculate the expected sum:** Use the formula `(n * (n + 1)) // 2` to instantly find the sum of all integers from `0` up to `n` in O(1) time. 
3. **Calculate the actual sum:** Sum the numbers that are currently present in the array using Python's built-in, highly optimized `sum()` function.
4. **Find the difference:** Subtract the actual sum from the expected sum and return the result. 

## Complexity
- **Time:** O(n) - We do a single pass over the array to calculate `sum(nums)`. Calculating the expected sum takes O(1) time.
- **Space:** O(1) - We only store a few integer variables, requiring constant extra memory regardless of the array's size.
