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
