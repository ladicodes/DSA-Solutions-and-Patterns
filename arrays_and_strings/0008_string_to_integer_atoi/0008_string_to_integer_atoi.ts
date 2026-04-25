// 8. String to Integer (atoi)
//
// Implement atoi which converts a string to a 32-bit signed integer.
// Rules (applied in order):
//   1. Ignore leading whitespace.
//   2. Read an optional '+' or '-' sign.
//   3. Read as many digit characters as possible.
//   4. Stop at the first non-digit (no error).
//   5. Clamp to [−2^31, 2^31 − 1] if out of range.
//
// Example: "   -42abc" -> -42
// Example: "4193 with words" -> 4193
// Example: "words 987" -> 0

// --- Original Solution ---
// Uses a Map<string, number> to recognise digit characters.
// Correct, but a character range check (ch >= '0' && ch <= '9') is lighter
// and avoids the upfront Map construction.
//
// function myAtoiOriginal(s: string): number {
//     const INT_MIN = -(2 ** 31);
//     const INT_MAX = (2 ** 31) - 1;
//     const digits = new Map([['0',0],['1',1],['2',2],['3',3],['4',4],
//                             ['5',5],['6',6],['7',7],['8',8],['9',9]]);
//     const sTrim = s.trim();
//     let newS = '';
//     let sign = 1;
//     for (let i = 0; i < sTrim.length; i++) {
//         if (!digits.has(sTrim[i])) {
//             if (i === 0 && (sTrim[i] === '-' || sTrim[i] === '+')) {
//                 sign = sTrim[i] === '-' ? -1 : 1;
//                 continue;
//             } else { break; }
//         } else { newS += sTrim[i]; }
//     }
//     const rs = sign * Number(newS);
//     if (rs < INT_MIN) return INT_MIN;
//     if (rs > INT_MAX) return INT_MAX;
//     return rs;
// }

// --- Optimised Solution ---
// Same algorithm, character range check instead of Map.
// Accumulates the number as an integer directly to avoid a second parse step.

function myAtoi(s: string): number {
    const INT_MIN = -(2 ** 31);
    const INT_MAX = 2 ** 31 - 1;

    let i = 0;
    const n = s.length;

    // Step 1: skip leading whitespace.
    while (i < n && s[i] === ' ') i++;

    // Step 2: read optional sign.
    let sign = 1;
    if (i < n && (s[i] === '+' || s[i] === '-')) {
        if (s[i] === '-') sign = -1;
        i++;
    }

    // Step 3 & 4: read digits, stop at first non-digit.
    let result = 0;
    while (i < n && s[i] >= '0' && s[i] <= '9') {
        result = result * 10 + (s[i].charCodeAt(0) - 48);
        i++;
    }

    // Step 5: apply sign and clamp to 32-bit signed range.
    result *= sign;
    if (result < INT_MIN) return INT_MIN;
    if (result > INT_MAX) return INT_MAX;
    return result;
}

/*
Walkthrough — s = "  -4193 with words"

i=0,1: skip spaces -> i=2
i=2: '-' -> sign=-1, i=3
i=3: '4' digit -> result=4,  i=4
i=4: '1' digit -> result=41, i=5
i=5: '9' digit -> result=419, i=6
i=6: '3' digit -> result=4193, i=7
i=7: ' ' not a digit -> stop

result = -1 * 4193 = -4193
-4193 is within [-2147483648, 2147483647] -> return -4193

---

Clamp example — s = "99999999999"

result accumulates to 99999999999
99999999999 > INT_MAX (2147483647) -> return 2147483647

Time Complexity:  O(n) — single pass through the string
Space Complexity: O(1)
*/

export { myAtoi };
