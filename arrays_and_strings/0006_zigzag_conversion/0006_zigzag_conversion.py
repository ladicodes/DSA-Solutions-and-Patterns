"""6. Zigzag Conversion

Write the string in a zigzag pattern on a given number of rows, then read
line by line to produce the output.

Example: s = "PAYPALISHIRING", numRows = 3

  P   A   H   N
  A P L S I I G
  Y   I   R

Output: "PAHNAPLSIIGYIR"

Strategy: math-based row traversal (no simulation)
Characters repeat in cycles of length increment = 2 * (numRows - 1).
For row i, the vertical character in each cycle is at index j = i, i+increment, ...
Middle rows also have a diagonal character at j + increment - 2*i per cycle.
"""


def convert(s: str, numRows: int) -> str:
    # Single row or string shorter than the grid: no rearrangement needed.
    if numRows == 1 or numRows >= len(s):
        return s

    result = []
    increment = 2 * (numRows - 1)  # cycle length

    for i in range(numRows):
        j = i
        while j < len(s):
            # Every row has a vertical character at position j.
            result.append(s[j])

            # Middle rows additionally have a diagonal character per cycle.
            if 0 < i < numRows - 1:
                diagonal_index = j + increment - 2 * i
                if diagonal_index < len(s):
                    result.append(s[diagonal_index])

            j += increment

    return "".join(result)


"""
Walkthrough — s = "PAYPALISHIRING", numRows = 3

increment = 4

Row 0: j=0,4,8,12  -> P, A, H, N
Row 1: j=1  -> 'A', diagonal=3  -> 'P'
       j=5  -> 'L', diagonal=7  -> 'S'
       j=9  -> 'I', diagonal=11 -> 'I'
       j=13 -> 'G', diagonal=15 (out of bounds, skip)
Row 2: j=2,6,10    -> Y, I, R

Result: "PAHNAPLSIIGYIR"

Why diagonalIndex = j + increment - 2*i:
  Within a cycle, the vertical character for row i lands i steps in.
  Its zigzag mirror is (increment - i) steps in, so it sits
  (increment - i) - i = increment - 2*i positions after j.

Time Complexity:  O(n) — each character is visited exactly once
Space Complexity: O(n) — result list holds all n characters
"""
