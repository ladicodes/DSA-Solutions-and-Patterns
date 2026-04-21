// 2078. Two Furthest Houses With Different Colors
//
// There are n houses in a row, each painted with a color represented by colors[i].
// Return the maximum distance between two houses with different colors.
//
// Example: colors = [1,1,1,6,1,1,1] -> 3

// Strategy: greedy from both ends
// The furthest pair must involve either the first or last house.
// Two scans suffice:
//   1. Fix the last house, scan from the left for the first different color.
//   2. Fix the first house, scan from the right for the first different color.

package arrays

func maxDistance(colors []int) int {
	n := len(colors)

	// Scan from left: furthest house from the right end with a different color.
	i := 0
	for colors[i] == colors[n-1] {
		i++
	}
	dist1 := (n - 1) - i

	// Scan from right: furthest house from the left end with a different color.
	j := n - 1
	for colors[j] == colors[0] {
		j--
	}
	dist2 := j // j - 0

	if dist1 > dist2 {
		return dist1
	}
	return dist2
}

/*
Walkthrough — colors = [1,1,1,6,1,1,1]  (n = 7)

Scan from left (last house color = 1):
  i advances past indices 0,1,2 (all color 1), stops at i=3 (color 6)
  dist1 = 6 - 3 = 3

Scan from right (first house color = 1):
  j retreats past indices 6,5,4 (all color 1), stops at j=3 (color 6)
  dist2 = 3

Result: max(3, 3) = 3

Time Complexity:  O(n) — two linear scans, each at most n steps
Space Complexity: O(1)
*/
