"""8. String to Integer (atoi)

Implement atoi which converts a string to a 32-bit signed integer.
Rules: skip leading spaces, read optional sign, read digits, stop at
first non-digit, clamp to [−2^31, 2^31 − 1].

Example: "   -42abc" -> -42
Example: "4193 with words" -> 4193
Example: "words 987" -> 0
"""

INT_MIN = -(2**31)
INT_MAX = 2**31 - 1


def myAtoi(s: str) -> int:
    i = 0
    n = len(s)

    # Step 1: skip leading whitespace.
    while i < n and s[i] == ' ':
        i += 1

    # Step 2: read optional sign.
    sign = 1
    if i < n and s[i] in ('+', '-'):
        if s[i] == '-':
            sign = -1
        i += 1

    # Steps 3 & 4: read digits, stop at first non-digit.
    result = 0
    while i < n and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1

    # Step 5: apply sign and clamp to 32-bit signed range.
    result *= sign
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX
    return result


"""
Walkthrough — s = "  -4193 with words"

i=0,1: skip spaces -> i=2
i=2: '-' -> sign=-1, i=3
i=3..6: digits '4','1','9','3' -> result=4193
i=7: ' ' not a digit -> stop

result = -1 * 4193 = -4193 -> within range -> return -4193

---

Clamp example — s = "99999999999"

result accumulates to 99999999999 (Python int, no overflow)
99999999999 > INT_MAX -> return 2147483647

Note: Python integers have arbitrary precision so there is no native
overflow here — the clamp at the end handles the 32-bit boundary explicitly.

Time Complexity:  O(n) — single pass through the string
Space Complexity: O(1)
"""
