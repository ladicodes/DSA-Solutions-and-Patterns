// 20. Valid Parentheses
//
// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
// determine if the input string is valid.
//
// A string is valid if:
//   - Open brackets are closed by the same type of bracket.
//   - Open brackets are closed in the correct order.
//   - Every close bracket has a corresponding open bracket of the same type.

package arrays

func isValid(s string) bool {
	// Stack tracks unmatched opening brackets in the order they appeared.
	stack := []rune{}

	// Maps each closing bracket to the opening bracket it must match.
	matchingOpen := map[rune]rune{
		')': '(',
		'}': '{',
		']': '[',
	}

	for _, char := range s {
		if char == '(' || char == '{' || char == '[' {
			// Opening bracket: push and wait for its pair.
			stack = append(stack, char)
		} else {
			// Closing bracket: stack must be non-empty and top must match.
			if len(stack) == 0 || stack[len(stack)-1] != matchingOpen[char] {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}

	// Every opener must have been matched (stack empty = all closed).
	return len(stack) == 0
}

/*
Walkthrough Examples

--- Valid: "()[]{}" ---

char = '(' -> stack: ['(']
char = ')' -> top '(' == matchingOpen[')'] '(' ✓ -> stack: []
char = '[' -> stack: ['[']
char = ']' -> top '[' == matchingOpen[']'] '[' ✓ -> stack: []
char = '{' -> stack: ['{']
char = '}' -> top '{' == matchingOpen['}'] '{' ✓ -> stack: []
stack empty -> return true

--- Invalid: "([)]" ---

char = '(' -> stack: ['(']
char = '[' -> stack: ['(', '[']
char = ')' -> top '[' != matchingOpen[')'] '(' -> return false

Time Complexity:  O(n) — single pass through the string
Space Complexity: O(n) — stack holds at most n/2 opening brackets
*/
