# Problem: 143. Reorder List

## Link
https://leetcode.com/problems/reorder-list/

## Pattern
Fast & Slow Pointers / Linked List Reversal

## Intuition
This problem looks complex, but it's really just three smaller linked list problems combined. To get the alternating  pattern, we can divide the list in half (not neecessarily half in case of odd number of nodes), reverse the entire second half, and then merge the two halves together one node at a time.

## Approach (Step by Step)
1. **Divide into 2 halves:** Use a fast and slow pointer. The fast pointer moves twice as fast, so when it reaches the end, the slow pointer will be right at the middle of the list. We then break the link between the two halves.
2. **Reverse the 2nd half:** Using the usual reversal technique, flip the arrows of the second half so it points backwards.
3. **Merge:** Iterate through both halves at the same time, alternating the `.next` pointers to link them together.

## Complexity
- **Time:** O(n) - We pass through the list to find the middle, pass through the second half to reverse it, and pass through both to merge. All of these are linear operations.
- **Space:** O(1) - We are just rearranging existing pointers, so no extra memory is needed.
