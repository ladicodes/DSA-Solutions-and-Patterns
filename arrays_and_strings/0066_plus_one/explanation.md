# Problem: 66. Plus One

## Link
https://leetcode.com/problems/plus-one/

## Pattern
Array Manipulation / Math

## Intuition
Instead of using while loop or dealing with carry-overs digit by digit, we can convert the entire array into a single mathematical integer, add one to it, and then unpack the resulting integer back into an array of digits. 

## Approach (Step by Step)
1. **Calculate the integer value, and represent as a list:** Loop through the given array and multiply each digit by its corresponding base-10 place value (e.g., the first digit of `[1,2,3]` is multiplied by 100).
2. **Sum the values:** sum them to get the full number.
3. **Increment and Format the output:** add 1 to the calculated sum, convert the incremented integer into a string so we can iterate through each character, casting them back to integers to form our final list.

## Complexity
- Time: O(n) - We iterate through the digits array of size *n* to create the sum, and then iterate through a string of length *n* (or *n+1*) to build the answer.
- Space: O(n) - We create a new list of size *n* (or *n+1*) to store and return the final digits.
