"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
"""

"""
Logic:
Given a queue, we can use two stacks to implement it. 
We will use one stack (stk1) for enqueue operations and another stack (stk2) for dequeue operations. 
When we want to pop an element, we will transfer all elements from stk1 to stk2, which will reverse the order of the elements, allowing us to pop the front element of the queue. 
After popping, we will transfer the elements back to stk1.
"""



class MyQueue:

    def __init__(self): #Enquque with stk1 and dequeue with stk2
        self.stk1 = list()
        self.stk2 = list()

    def push(self, x: int) -> None:
        self.stk1.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.stk1)):
            curr = self.stk1.pop()
            self.stk2.append(curr)
        
        answer = self.stk2.pop()

        for i in range(len(self.stk2)):
            smth = self.stk2.pop()
            self.stk1.append(smth)

        return answer

    def peek(self) -> int:
        return self.stk1[0]
        

    def empty(self) -> bool:
        if len(self.stk1) == 0:
            return True #The stack really is empty
        return False
        


"""
Complexity Analysis:
Time Complexity: O(1) for enqueue, O(n) for dequeue, O(1) for peek, O(1) for empty
Space Complexity: O(n) for the two stacks
"""