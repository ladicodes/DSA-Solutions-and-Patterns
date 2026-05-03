// 796. Rotate String
//
// Given two strings s and goal, return true if and only if s can become goal
// after some number of shifts. A shift moves the last character to the front.
//
// Example: s = "abcde", goal = "cdeab" -> true  (shift 3 times)
// Example: s = "abcde", goal = "abced" -> false

// Strategy: simulate rotations
// Try every rotation (at most s.length of them). Each rotation moves the
// last character to the front. If any matches goal, return true.
//
// Note: an O(n) alternative is to check whether goal is a substring of s+s,
// since every rotation of s appears as a contiguous slice of s+s.
// Example: "abcde"+"abcde" = "abcdeabcde" contains "cdeab" -> true.

function rotateString(s: string, goal: string): boolean {
    if (s.length !== goal.length) return false;

    let newStr = s;

    for (let i = 0; i < s.length; i++) {
        if (newStr === goal) return true;
        // Move the last character to the front.
        newStr = newStr[newStr.length - 1] + newStr.slice(0, newStr.length - 1);
    }

    return false;
}

/*
Walkthrough — s = "abcde", goal = "cdeab"

i=0: newStr="abcde" != "cdeab" -> rotate -> "eabcd"
i=1: newStr="eabcd" != "cdeab" -> rotate -> "deabc"
i=2: newStr="deabc" != "cdeab" -> rotate -> "cdeab"
i=3: newStr="cdeab" == "cdeab" -> return true

Early exit: if s == goal (0 rotations needed), caught at i=0 before any rotation.

Edge case: s = "aa", goal = "aa" -> true immediately.
Edge case: different lengths -> false (guard at top).

Time Complexity:  O(n^2) — n rotations × O(n) string comparison and slice each
Space Complexity: O(n) — newStr holds a copy of s

O(n) alternative: (s + s).includes(goal)
*/

export { rotateString };
