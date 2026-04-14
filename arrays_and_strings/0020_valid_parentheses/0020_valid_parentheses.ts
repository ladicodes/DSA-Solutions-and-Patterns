// 20. Valid Parentheses
//
// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
// determine if the input string is valid.
//
// A string is valid if:
//   - Open brackets are closed by the same type of bracket.
//   - Open brackets are closed in the correct order.
//   - Every close bracket has a corresponding open bracket of the same type.

// --- Original Solution ---
// Uses a stack of string labels ("paren", "braces", "brackets") alongside
// three separate counters. The stack alone is sufficient — the counters are
// redundant — but the core idea (push on open, pop-and-check on close) is correct.
//
// function isValidOriginal(s: string): boolean {
//     let parenCount = 0;
//     let bracesCount = 0;
//     let bracketsCount = 0;
//     let activeBrackets: string[] = [];
//     for (let i = 0; i < s.length; i++) {
//         if (s[i] == '(')       { parenCount++;    activeBrackets.push('paren'); }
//         else if (s[i] == '{')  { bracesCount++;   activeBrackets.push('braces'); }
//         else if (s[i] == '[')  { bracketsCount++; activeBrackets.push('brackets'); }
//         else if (s[i] == ')' && activeBrackets[activeBrackets.length - 1] == 'paren')    { parenCount--;    activeBrackets.pop(); }
//         else if (s[i] == '}' && activeBrackets[activeBrackets.length - 1] == 'braces')   { bracesCount--;   activeBrackets.pop(); }
//         else if (s[i] == ']' && activeBrackets[activeBrackets.length - 1] == 'brackets') { bracketsCount--; activeBrackets.pop(); }
//         else { parenCount--; }
//     }
//     return activeBrackets.length == 0 && parenCount == 0 && bracesCount == 0 && bracketsCount == 0;
// }

// --- Optimised Solution ---
// Drop the three counters entirely: the stack already captures whether every
// opener has been closed in order. Push opening brackets; for each closing
// bracket, pop and verify the match. If the stack is empty at the end, the
// string is valid.

function isValid(s: string): boolean {
    // Stack tracks unmatched opening brackets in the order they appeared.
    const stack: string[] = [];

    // Maps each closing bracket to the opening bracket it must match.
    const matchingOpen: Record<string, string> = {
        ')': '(',
        '}': '{',
        ']': '[',
    };

    for (const char of s) {
        if (char === '(' || char === '{' || char === '[') {
            // Opening bracket: push and wait for its pair.
            stack.push(char);
        } else {
            // Closing bracket: the most recent opener must match.
            // stack.pop() returns undefined on an empty stack, which also
            // fails the comparison — handles the "extra closing bracket" case.
            if (stack.pop() !== matchingOpen[char]) {
                return false;
            }
        }
    }

    // Every opener must have been matched (stack empty = all closed).
    return stack.length === 0;
}

/*
Walkthrough Examples

--- Valid: "()[]{}" ---

char = '(' -> stack: ['(']
char = ')' -> pop '(' === matchingOpen[')'] '(' ✓ -> stack: []
char = '[' -> stack: ['[']
char = ']' -> pop '[' === matchingOpen[']'] '[' ✓ -> stack: []
char = '{' -> stack: ['{']
char = '}' -> pop '{' === matchingOpen['}'] '{' ✓ -> stack: []
stack empty -> return true

--- Invalid: "([)]" ---

char = '(' -> stack: ['(']
char = '[' -> stack: ['(', '[']
char = ')' -> pop '[' !== matchingOpen[')'] '(' -> return false

--- Invalid: "{[]" (unclosed opener) ---

char = '{' -> stack: ['{']
char = '[' -> stack: ['{', '[']
char = ']' -> pop '[' === matchingOpen[']'] '[' ✓ -> stack: ['{']
End of string, stack not empty -> return false

Time Complexity:  O(n) — single pass through the string
Space Complexity: O(n) — stack holds at most n/2 opening brackets
*/

export { isValid };
