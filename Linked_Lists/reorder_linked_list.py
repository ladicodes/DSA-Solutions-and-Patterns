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

## Code
```python
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s_ptr, f_ptr = head, head.next

        # divide into 2 halves
        while f_ptr and f_ptr.next:
            f_ptr = f_ptr.next.next # fast moves twice as fast to reach the end
            s_ptr = s_ptr.next # leaving slow at the middle

        half2 = s_ptr.next # start of the second half
        s_ptr.next = None # break the link to split the list into two halves and set the end to None
        prev = s_ptr.next # since s_ptr.next is now None, this acts to create an extra empty bucket-like scenario

        # reverse 2nd half
        while half2:
            nxt = half2.next # step 3 needed to get this value not manipulated already by step 1
            half2.next = prev # step 1 to flip the arrow (i.e the link in the linkedlist)
            prev = half2 # step 2 to move prev one step further into the linkedlist
            half2 = nxt # step 4 to continue the reversal for the next value.

        # merge
        half1, half2 = head, prev # prev is now the head of our reversed 2nd half
        while half2:
            tmp1, tmp2 = half1.next, half2.next # save the next values before we break their links
            half1.next = half2 # link current half1 node to current half2 node
            half2.next = tmp1 # link current half2 node back to the next half1 node
            half1, half2 = tmp1, tmp2 # move both forward to continue the merge

**Example 1:**
> **Input:** `head = [1,2,3,4]`
> **Output:** `[1,4,2,3]`

**Example 2:**
> **Input:** `head = [2,4,6,8,10]`
> **Output:** `[2,10,4,8,6]`
