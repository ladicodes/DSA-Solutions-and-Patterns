// 17. Letter Combinations of a Phone Number
//
// Given a string containing digits 2-9, return all possible letter combinations
// that the number could represent on a phone keypad.
// Return an empty array if the input is empty.
//
// Example: "23" -> ["ad","ae","af","bd","be","bf","cd","ce","cf"]

// Strategy: backtracking
// For each digit we pick one of its mapped letters and recurse on the next digit.
// A path is complete when the built string matches the length of the input.

package backtracking

var keypadMap = map[byte][]string{
	'2': {"a", "b", "c"},
	'3': {"d", "e", "f"},
	'4': {"g", "h", "i"},
	'5': {"j", "k", "l"},
	'6': {"m", "n", "o"},
	'7': {"p", "q", "r", "s"},
	'8': {"t", "u", "v"},
	'9': {"w", "x", "y", "z"},
}

func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}

	result := []string{}
	letterCombinationsBacktrack(digits, &result, "", 0)
	return result
}

func letterCombinationsBacktrack(digits string, result *[]string, current string, index int) {
	// Base case: one letter chosen per digit — combination is complete.
	if len(current) == len(digits) {
		*result = append(*result, current)
		return
	}

	letters := keypadMap[digits[index]]

	// Try each letter mapped to the current digit and recurse on the next.
	for _, letter := range letters {
		letterCombinationsBacktrack(digits, result, current+letter, index+1)
	}
}

/*
Walkthrough — digits = "23"

letterCombinations("23")
backtrack("23", [], "", 0)
  digit '2' -> ["a","b","c"]
  "a" -> backtrack("23", [], "a", 1)
    digit '3' -> ["d","e","f"]
    "d" -> len==2 -> append "ad"
    "e" -> len==2 -> append "ae"
    "f" -> len==2 -> append "af"
  "b" -> append "bd","be","bf"
  "c" -> append "cd","ce","cf"

Result: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Time Complexity:  O(4^n * n) — at most 4 branches per digit, n digits deep,
                  and each leaf copies a string of length n
Space Complexity: O(n) — recursion depth equals the number of digits
*/
