# Problem: 141. Linked List Cycle

## Link
https://leetcode.com/problems/linked-list-cycle/

## Pattern
Fast & Slow Pointers

## Intuition
Think of two runners on a track. If the track is a straight line, the faster runner will eventually reach the finish line. However, if the track has a loop (a cycle), the faster runner will just keep running in circles and will eventually "lap" or catch up from behind and collide with the slower runner. 

## Approach (Step by Step)
1. **Initialize pointers:** Create two pointers, `slow_ptr` and `fast_ptr`, and set both to the `head` of the linked list.
2. **Traverse the list:** Use a `while` loop that continues as long as `fast_ptr` and `fast_ptr.next` are not `None`. This prevents trying to access properties of a `None` object when we reach the end of a straight list.
3. **Move at different speeds:** Move `slow_ptr` forward by one node, and `fast_ptr` forward by two nodes.
4. **Check for collision:** If `slow_ptr` and `fast_ptr` ever meet at the same node, a cycle exists. Return `True`.
5. **End of list:** If the loop terminates naturally, it means the `fast_ptr` hit the end of the list, confirming there is no cycle. Return `False`.

## Complexity
- Time: O(n) - We visit each node. If there is no cycle, we traverse the list once. If there is a cycle, the fast pointer will catch up to the slow pointer in at most $n$ steps.
- Space: O(1) - We only use two pointers, requiring constant extra space regardless of the list size.

## Code
```python
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize both pointers at the start
        slow_ptr, fast_ptr = head, head

        # Loop until fast_ptr reaches the end of the list
        # Checking fast_ptr.next ensures we don't call next.next on a None object
        while fast_ptr and fast_ptr.next: 
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            # If the fast pointer laps the slow pointer, there is a cycle
            if slow_ptr == fast_ptr:
                return True

        # If we reach here, we hit the end of the list (no cycle)
        return False
