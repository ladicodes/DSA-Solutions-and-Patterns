/**
Problem
2: You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
Explanation: 9999999 + 9999 = 10009998.

*/

class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    //reverse the list
    function reverse(list: ListNode | null) {
        let curr = list
        let prev: ListNode | null = null

        while (curr) {
            let tmp = curr.next
            curr.next = prev
            prev = curr

            curr = tmp
        }

        return prev
    }

    const rev_l1 = reverse(l1)
    const rev_l2 = reverse(l2)

    // Split to numbers
    function split_to_numbers(list: ListNode | null) {
        let curr = list
        let num: string = ''
        while (curr) {
            num += curr.val

            curr = curr.next
        }

        return BigInt(num)
    }

    //Get sum
    const num_l1 = split_to_numbers(rev_l1)
    const num_l2 = split_to_numbers(rev_l2)

    const sum = num_l1 + num_l2


    // Map the sum to a new list
    function sum_to_new_list(n: BigInt){
        const digits = String(n).split('').map(Number)

        const dummy = new ListNode()
        let curr = dummy

        for(const d of digits){
            curr.next = new ListNode(d)
            curr = curr.next
        }

        return dummy.next
    }
    const res = sum_to_new_list(sum)

    return reverse(res)
};

/**

Walkthrough Example
Input:
  l1 = [2,4,3]  → represents 342  (stored in reverse order)
  l2 = [5,6,4]  → represents 465  (stored in reverse order)

Step 1 — Reverse both lists:
  rev_l1 = [3,4,2]
  rev_l2 = [4,6,5]

Step 2 — Read digits left-to-right to form numbers:
  num_l1 = BigInt("342") = 342n
  num_l2 = BigInt("465") = 465n

Step 3 — Add:
  sum = 342n + 465n = 807n

Step 4 — Map sum to a new list (digits left-to-right):
  "807" → [8,0,7]
  res = 8 → 0 → 7

Step 5 — Reverse result (to match expected reversed output):
  reverse([8,0,7]) = [7,0,8]

Final Result: [7,0,8]  ✓ (represents 807)

---
Why BigInt?
  The linked lists can be arbitrarily long, meaning the number they represent
  can exceed Number.MAX_SAFE_INTEGER (2^53 - 1). BigInt handles integers of
  any size without precision loss.

---
Complexity
  Time Complexity:  O(n + m)  — where n and m are the lengths of l1 and l2;
                               each list is traversed a constant number of times
  Space Complexity: O(n + m)  — for the output linked list and intermediate strings

*/
