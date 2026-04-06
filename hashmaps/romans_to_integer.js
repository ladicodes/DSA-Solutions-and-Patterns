/** 
Problem
13: Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4. 

*/

function romanToInt(s) {
  //check if the numeric character is less than the one before it
  const map = new Map();
  map.set("I", 1);
  map.set("V", 5);
  map.set("X", 10);
  map.set("L", 50);
  map.set("C", 100);
  map.set("D", 500);
  map.set("M", 1000);

  let sum = 0;
  for (let i = s.length - 1; i >= 0; i--) {
    if (map.has(s[i])) {
      if (i !== s.length - 1) {
        if (map.get(s[i]) < map.get(s[i + 1])) {
          sum -= map.get(s[i]);
          continue;
        }
      }
      sum += map.get(s[i]);
    }
  }

  return sum;
}

console.log(romanToInt("LVIII"));

/**
 
Walkthrough Example
Input:
  s = "LVIII"

Map setup:
  I → 1   V → 5   X → 10   L → 50
  C → 100   D → 500   M → 1000

We iterate RIGHT TO LEFT (i = 4 → 0), comparing each character
to the one immediately to its right (i+1).

  sum = 0

Step 1 (i = 4):
  s[4] = 'I' → value = 1
  i == s.length - 1, so no right neighbour to compare
  → add → sum = 0 + 1 = 1

Step 2 (i = 3):
  s[3] = 'I' → value = 1
  s[4] = 'I' → right value = 1
  1 < 1? No
  → add → sum = 1 + 1 = 2

Step 3 (i = 2):
  s[2] = 'I' → value = 1
  s[3] = 'I' → right value = 1
  1 < 1? No
  → add → sum = 2 + 1 = 3

Step 4 (i = 1):
  s[1] = 'V' → value = 5
  s[2] = 'I' → right value = 1
  5 < 1? No
  → add → sum = 3 + 5 = 8

Step 5 (i = 0):
  s[0] = 'L' → value = 50
  s[1] = 'V' → right value = 5
  50 < 5? No
  → add → sum = 8 + 50 = 58

Final Result: 58

---
Subtraction case (how IV = 4 would work):
  s = "IV"

  i = 1: s[1] = 'V' → no right neighbour → add → sum = 5
  i = 0: s[0] = 'I' → value = 1
         s[1] = 'V' → right value = 5
         1 < 5? Yes → subtract → sum = 5 - 1 = 4

  Result: 4

  The reason we subtract when value < rightValue is because - in roman numeral, whenever a smaller numeral appears directly before a larger one, it means subtraction. It is an observable pattern
  e.g IX = 9 - I=1, X=10 - 1 is less than 10. so we subtract

---
Complexity
  Time Complexity:  O(n)  — single pass through the string
  Space Complexity: O(1)  — map is fixed-size (7 entries)


 */
