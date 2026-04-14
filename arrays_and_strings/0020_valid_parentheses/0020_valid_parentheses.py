"""20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A string is valid if:
  - Open brackets are closed by the same type of bracket.
  - Open brackets are closed in the correct order.
  - Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # Stack tracks unmatched opening brackets in the order they appeared.
        stack = []

        # Maps each closing bracket to the opening bracket it must match.
        matching_open = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in '({[':
                # Opening bracket: push and wait for its pair.
                stack.append(char)
            else:
                # Closing bracket: stack must be non-empty and top must match.
                if not stack or stack[-1] != matching_open[char]:
                    return False
                stack.pop()

        # Every opener must have been matched (stack empty = all closed).
        return len(stack) == 0


"""
Walkthrough Examples

--- Valid: "()[]{}" ---

char = '(' -> stack: ['(']
char = ')' -> top '(' == matching_open[')'] '(' ✓ -> stack: []
char = '[' -> stack: ['[']
char = ']' -> top '[' == matching_open[']'] '[' ✓ -> stack: []
char = '{' -> stack: ['{']
char = '}' -> top '{' == matching_open['}'] '{' ✓ -> stack: []
stack empty -> return True

--- Invalid: "([)]" ---

char = '(' -> stack: ['(']
char = '[' -> stack: ['(', '[']
char = ')' -> top '[' != matching_open[')'] '(' -> return False

--- Invalid: "{[]" (unclosed opener) ---

char = '{' -> stack: ['{']
char = '[' -> stack: ['{', '[']
char = ']' -> top '[' == matching_open[']'] '[' ✓ -> stack: ['{']
End of string, stack not empty -> return False

Time Complexity:  O(n) — single pass through the string
Space Complexity: O(n) — stack holds at most n/2 opening brackets
"""
