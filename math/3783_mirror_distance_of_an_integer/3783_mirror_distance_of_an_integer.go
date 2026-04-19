// 3783. Mirror Distance of an Integer
//
// The mirror of an integer is obtained by reversing its digits.
// Return the absolute difference between n and its mirror.
//
// Example: n = 1234 -> mirror = 4321 -> |1234 - 4321| = 3087

// Strategy: digit reversal via repeated modulo extraction
// Pull digits off the right of n one at a time and build the reversed number
// by shifting the result left (×10) before appending each digit.

package math

func mirrorDistance(n int) int {
	return abs(n - flipInt(n))
}

func flipInt(n int) int {
	result := 0

	for n > 0 {
		digit := n % 10         // peel the rightmost digit
		result = result*10 + digit // shift result left, append digit
		n /= 10                 // drop the rightmost digit
	}

	return result
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

/*
Walkthrough — n = 1234

iteration 1: digit = 4,  result = 4,    n = 123
iteration 2: digit = 3,  result = 43,   n = 12
iteration 3: digit = 2,  result = 432,  n = 1
iteration 4: digit = 1,  result = 4321, n = 0

flipInt(1234) = 4321
mirrorDistance = |1234 - 4321| = 3087

Edge case — palindrome: n = 121
flipInt(121) = 121
mirrorDistance = |121 - 121| = 0

Time Complexity:  O(d) where d = number of digits in n  (d = floor(log10(n)) + 1)
Space Complexity: O(1)
*/
