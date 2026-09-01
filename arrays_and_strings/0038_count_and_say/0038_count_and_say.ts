// 38. Count and Say
//
// The count-and-say sequence is built by reading the previous term aloud:
//   1     -> "1"
//   2     -> "11"      (one 1)
//   3     -> "21"      (two 1s)
//   4     -> "1211"    (one 2, one 1)
//   5     -> "111221"  (one 1, one 2, two 1s)
//
// Given n, return the nth term of the sequence.

// Strategy: iterative run-length encoding
// Build the sequence one step at a time. Each step calls `pairs`, which
// scans the current string and encodes consecutive runs as "count + digit".
// Two triggers write a run to output:
//   1. The digit changes   — flush the completed run, start a new one.
//   2. End of string       — flush the final run (no digit change to trigger it).

function countAndSay(n: number): string {
    if (n === 1) return '1';

    let term = '1';
    for (let i = 1; i < n; i++) {
        term = encode(term);
    }
    return term;
}

function encode(s: string): string {
    let out = '';
    let curr = s[0];
    let count = 1;

    for (let i = 1; i < s.length; i++) {
        if (s[i] === curr) {
            count++;
        } else {
            // Digit changed: flush the current run.
            out += count + curr;
            curr = s[i];
            count = 1;
        }
    }
    // Flush the final run (no digit change triggers it).
    out += count + curr;

    return out;
}

/*
Walkthrough — n = 5, building term by term:

term 1: "1"
term 2: encode("1")
  i=end: flush -> "1"+"1" = "11"
term 3: encode("11")
  i=1: '1'=='1' -> count=2
  i=end: flush -> "2"+"1" = "21"
term 4: encode("21")
  i=1: '1'!='2' -> flush "12", curr='1', count=1
  i=end: flush -> "12"+"11" = "1211"
term 5: encode("1211")
  i=1: '2'!='1' -> flush "11", curr='2', count=1
  i=2: '1'!='2' -> flush "12", curr='1', count=1
  i=3: '1'=='1' -> count=2
  i=end: flush -> "1112"+"21" = "111221"

Result: "111221"

Why the final flush moved out of the loop:
  The original solution used an `if (i == nStr.length - 1)` check inside
  the loop body to handle the last run — this works but runs on every
  iteration. Placing it after the loop is cleaner and only runs once.

Time Complexity:  O(n * m) where m is the length of the nth term
                  (each term can grow, but is bounded in practice)
Space Complexity: O(m) — one term stored at a time
*/

export { countAndSay };
