'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
'''
class Solution(object):
    def reverseList(self, head):
        # iterative in-place reversal using three pointers
        curr, prev = head, None  # curr walks forward, prev becomes new head
        while curr:
            nxt_node = curr.next     # temporarily store next node
            curr.next = prev         # reverse the link
            prev = curr              # move prev forward
            curr = nxt_node          # move curr forward using stored next

        # prev is the new head of the reversed list
        return prev

# Walkthrough Example:
# head: 1 -> 2 -> 3 -> None
# Step 1: reverse 1's pointer to None, prev=1, curr=2
# Step 2: reverse 2's pointer to 1, prev=2, curr=3
# Final: prev points to 3 -> 2 -> 1 -> None

# Time Complexity: O(n) — each node visited once.
# Space Complexity: O(1) — in-place reversal with constant extra pointers.