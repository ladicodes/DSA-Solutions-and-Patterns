// 8. String to Integer (atoi)
//
// Implement atoi which converts a string to a 32-bit signed integer.
// Rules: skip leading spaces, read optional sign, read digits, stop at
// first non-digit, clamp to [−2^31, 2^31 − 1].
//
// Example: "   -42abc" -> -42
// Example: "4193 with words" -> 4193

package arrays

import "math"

func myAtoi(s string) int {
	i := 0
	n := len(s)

	// Step 1: skip leading whitespace.
	for i < n && s[i] == ' ' {
		i++
	}

	// Step 2: read optional sign.
	sign := 1
	if i < n && (s[i] == '+' || s[i] == '-') {
		if s[i] == '-' {
			sign = -1
		}
		i++
	}

	// Steps 3 & 4: read digits, stop at first non-digit.
	result := 0
	for i < n && s[i] >= '0' && s[i] <= '9' {
		result = result*10 + int(s[i]-'0')
		i++
	}

	// Step 5: apply sign and clamp to 32-bit signed range.
	result *= sign
	if result < math.MinInt32 {
		return math.MinInt32
	}
	if result > math.MaxInt32 {
		return math.MaxInt32
	}
	return result
}

/*
Walkthrough — s = "  -4193 with words"

i=0,1: skip spaces -> i=2
i=2: '-' -> sign=-1, i=3
i=3..6: digits '4','1','9','3' -> result=4193
i=7: ' ' not a digit -> stop

result = -1 * 4193 = -4193 -> within range -> return -4193

Time Complexity:  O(n) — single pass through the string
Space Complexity: O(1)
*/
