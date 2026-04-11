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
