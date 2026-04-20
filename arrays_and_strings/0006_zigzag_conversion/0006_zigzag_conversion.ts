// 6. Zigzag Conversion
//
// Write the string in a zigzag pattern on a given number of rows, then read
// line by line to produce the output.
//
// Example: s = "PAYPALISHIRING", numRows = 3
//
//   P   A   H   N
//   A P L S I I G
//   Y   I   R
//
// Output: "PAHNAPLSIIGYIR"

// Strategy: math-based row traversal (no simulation)
// Simulating the zigzag would require O(numRows * cycle) extra space.
// Instead, observe that characters repeat in cycles of length:
//   increment = 2 * (numRows - 1)
//
// For row i, the "straight-down" character in each cycle is at index:
//   j = i, i + increment, i + 2*increment, ...
//
// Middle rows (not first, not last) also have a diagonal character per cycle,
// sitting at the mirror position within the cycle:
//   diagonalIndex = j + increment - 2*i
//
// We collect characters row by row in this order — no 2D grid needed.

function convert(s: string, numRows: number): string {
    // Single row or string shorter than the grid: no rearrangement needed.
    if (numRows === 1 || numRows >= s.length) return s;

    const result: string[] = [];
    const increment = 2 * (numRows - 1); // cycle length

    for (let i = 0; i < numRows; i++) {
        for (let j = i; j < s.length; j += increment) {
            // Every row has a "vertical" character at position j.
            result.push(s[j]);

            // Middle rows additionally have a diagonal character per cycle.
            if (i > 0 && i < numRows - 1) {
                const diagonalIndex = j + increment - 2 * i;
                if (diagonalIndex < s.length) {
                    result.push(s[diagonalIndex]);
                }
            }
        }
    }

    return result.join('');
}

/*
Walkthrough — s = "PAYPALISHIRING", numRows = 3

increment = 2 * (3 - 1) = 4

Indices:  0  1  2  3  4  5  6  7  8  9  10 11 12 13
Chars:    P  A  Y  P  A  L  I  S  H  I  R  I  N  G

Row 0 (first):  j = 0,4,8,12 -> P, A, H, N
Row 1 (middle): j = 1  -> s[1]='A', diagonal = 1+4-2=3  -> s[3]='P'
                j = 5  -> s[5]='L', diagonal = 5+4-2=7  -> s[7]='S'
                j = 9  -> s[9]='I', diagonal = 9+4-2=11 -> s[11]='I'
                j = 13 -> s[13]='G', diagonal = 13+4-2=15 (out of bounds, skip)
Row 2 (last):   j = 2,6,10 -> Y, I, R

Result: "PAHN" + "APLSIIG" + "YIR" = "PAHNAPLSIIGYIR"

Why diagonalIndex = j + increment - 2*i:
  Within a cycle of length `increment`, the vertical character for row i
  is `i` steps into the cycle. Its diagonal mirror is `increment - i` steps
  in, which is `increment - i - i = increment - 2*i` positions after j.

Time Complexity:  O(n) — each character is visited exactly once
Space Complexity: O(n) — result array holds all n characters
*/

export { convert };
