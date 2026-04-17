// 17. Letter Combinations of a Phone Number
//
// Given a string containing digits 2-9, return all possible letter combinations
// that the number could represent on a phone keypad.
// Return an empty array if the input is empty.
//
// Example: "23" -> ["ad","ae","af","bd","be","bf","cd","ce","cf"]

// Strategy: backtracking
// For each digit we pick one of its mapped letters and recurse on the next digit.
// The recursion depth equals the number of digits, and at each level we branch
// over however many letters that digit maps to (3 or 4).
// A path is complete when the built string matches the length of the input.

const keypadMap: Record<string, string[]> = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
};

function letterCombinations(digits: string): string[] {
    if (digits.length === 0) return [];

    const result: string[] = [];
    backtrack(digits, result, '', 0);
    return result;
}

function backtrack(
    digits: string,
    result: string[],
    current: string, // combination built so far
    index: number    // which digit we are currently expanding
): void {
    // Base case: we've picked one letter per digit — combination is complete.
    if (current.length === digits.length) {
        result.push(current);
        return;
    }

    const letters = keypadMap[digits[index]];

    // Try each letter mapped to the current digit and recurse on the next.
    for (const letter of letters) {
        backtrack(digits, result, current + letter, index + 1);
    }
}

/*
Walkthrough — digits = "23"

letterCombinations("23")
backtrack("23", [], "", 0)
  digit "2" -> letters ["a","b","c"]
  letter "a" -> backtrack("23", [], "a", 1)
    digit "3" -> letters ["d","e","f"]
    letter "d" -> backtrack("23", [], "ad", 2)  len==2 -> push "ad"
    letter "e" -> backtrack("23", [], "ae", 2)  len==2 -> push "ae"
    letter "f" -> backtrack("23", [], "af", 2)  len==2 -> push "af"
  letter "b" -> backtrack("23", [], "b", 1)
    -> push "bd", "be", "bf"
  letter "c" -> backtrack("23", [], "c", 1)
    -> push "cd", "ce", "cf"

Result: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Decision tree shape (digits = "23"):
              ""
           /  |  \
          a   b   c       <- digit "2"
        / | \ ...
       d  e  f            <- digit "3"

Time Complexity:  O(4^n * n) — at most 4 branches per digit, n digits deep,
                  and each leaf copies a string of length n
Space Complexity: O(n) — recursion depth equals the number of digits
*/

export { letterCombinations };
