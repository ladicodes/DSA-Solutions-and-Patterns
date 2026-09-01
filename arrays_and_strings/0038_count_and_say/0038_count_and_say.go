// 38. Count and Say
//
// The count-and-say sequence is built by reading the previous term aloud:
//   1 -> "1",  2 -> "11",  3 -> "21",  4 -> "1211",  5 -> "111221"
//
// Given n, return the nth term of the sequence.

// Strategy: iterative run-length encoding
// Each step encodes the previous term: scan for consecutive runs of the same
// digit and write "count + digit" for each run.

package arrays

import (
	"strconv"
	"strings"
)

func countAndSay(n int) string {
	if n == 1 {
		return "1"
	}

	term := "1"
	for i := 1; i < n; i++ {
		term = encode(term)
	}
	return term
}

func encode(s string) string {
	var out strings.Builder
	curr := s[0]
	count := 1

	for i := 1; i < len(s); i++ {
		if s[i] == curr {
			count++
		} else {
			// Digit changed: flush the current run.
			out.WriteString(strconv.Itoa(count))
			out.WriteByte(curr)
			curr = s[i]
			count = 1
		}
	}
	// Flush the final run.
	out.WriteString(strconv.Itoa(count))
	out.WriteByte(curr)

	return out.String()
}

/*
Walkthrough — n = 5

"1" -> "11" -> "21" -> "1211" -> "111221"

encode("1211"):
  i=1: '2'!='1' -> flush "1","1", curr='2', count=1
  i=2: '1'!='2' -> flush "1","2", curr='1', count=1
  i=3: '1'=='1' -> count=2
  after loop: flush "2","1"
  out: "11" + "12" + "21" = "111221"

Time Complexity:  O(n * m) where m is the length of the nth term
Space Complexity: O(m) — one term stored at a time
*/
