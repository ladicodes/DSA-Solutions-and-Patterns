// 58. Length of Last Word
//
// Given a string s consisting of words and spaces, return the length of the
// last word in the string.
//
// A word is a maximal substring consisting of non-space characters only.
//
// Example 1:
//   Input:  s = "Hello World"
//   Output: 5
//   Explanation: The last word is "World" with length 5.
//
// Example 2:
//   Input:  s = "   fly me   to   the moon  "
//   Output: 4
//   Explanation: The last word is "moon" with length 4.
//
// Example 3:
//   Input:  s = "luffy is still joyboy"
//   Output: 6
//   Explanation: The last word is "joyboy" with length 6.

package arrays

import "strings"

func lengthOfLastWord(s string) int {
	// Split the string on whitespace, discarding empty tokens from leading/trailing spaces.
	words := strings.Fields(s)

	// Return the length of the last word.
	return len(words[len(words)-1])
}

/*
Walkthrough Example

s = "   fly me   to   the moon  "

strings.Fields strips leading/trailing spaces and splits on any whitespace:
  words = ["fly", "me", "to", "the", "moon"]

Last element: words[4] = "moon"
len("moon") = 4

Return: 4

Note: strings.Fields is preferred over strings.Split(s, " ") here because
it correctly handles multiple consecutive spaces and leading/trailing spaces
without producing empty strings.

Time Complexity:  O(n) — entire string is scanned once
Space Complexity: O(n) — slice holds all the words
*/
