// 3783. Mirror Distance of an Integer
//
// The mirror of an integer is obtained by reversing its digits.
// Return the absolute difference between n and its mirror.
//
// Example: n = 1234 -> mirror = 4321 -> |1234 - 4321| = 3087

// Strategy: digit reversal via repeated modulo extraction
// Pull digits off the right of n one at a time and build the reversed number
// by shifting the result left (×10) before appending each digit.
// The | 0 trick is a bitwise floor — faster than Math.floor for positive integers.

function mirrorDistance(n: number): number {
    return Math.abs(n - flipInt(n));
}

function flipInt(n: number): number {
    let result = 0;

    while (n > 0) {
        const digit = n % 10;          // peel the rightmost digit
        result = result * 10 + digit;  // shift result left, append digit
        n = n / 10 | 0;               // drop the rightmost digit (fast floor)
    }

    return result;
}

/*
Walkthrough — n = 1234

iteration 1: digit = 1234 % 10 = 4,  result = 0*10+4 = 4,    n = 123
iteration 2: digit = 123  % 10 = 3,  result = 4*10+3 = 43,   n = 12
iteration 3: digit = 12   % 10 = 2,  result = 43*10+2 = 432, n = 1
iteration 4: digit = 1    % 10 = 1,  result = 432*10+1 = 4321, n = 0

flipInt(1234) = 4321
mirrorDistance = |1234 - 4321| = 3087

Edge case — palindrome: n = 121
flipInt(121) = 121
mirrorDistance = |121 - 121| = 0

Time Complexity:  O(d) where d = number of digits in n  (d = floor(log10(n)) + 1)
Space Complexity: O(1)
*/

export { mirrorDistance };
