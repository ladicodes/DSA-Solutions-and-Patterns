"""
Logic:
Given a stack, we can use two queues to implement it.
We will use one queue (q1) as our main storage and another queue (q2) as a temporary buffer.
When we want to push an element, we will first add it to q2. Then, we will transfer all elements from q1 to q2. This ensures that the newly added element is always at the front of q2, preserving the Last-In-First-Out (LIFO) order. Finally, we swap the names of q1 and q2.
"""

class MyStack:

    def __init__(self): #Main storage with q1 and temporary buffer with q2
        from collections import deque
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # Push element x to the temporary queue
        self.q2.append(x)
        
        # Transfer all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
            
        # Swap q1 and q2 so q1 always holds the elements in stack order
        self.q1, self.q2 = self.q2, self.q1
        

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]
        

    def empty(self) -> bool:
        if len(self.q1) == 0:
            return True #The queue really is empty
        return False
        
"""
Complexity Analysis:
Time Complexity: O(n) for push, O(1) for pop, O(1) for top, O(1) for empty
Space Complexity: O(n) for the two queues
"""