"""38. Count and Say

The count-and-say sequence is built by reading the previous term aloud:
  1 -> "1",  2 -> "11",  3 -> "21",  4 -> "1211",  5 -> "111221"

Given n, return the nth term of the sequence.

Strategy: iterative run-length encoding
Each step encodes the previous term: scan for consecutive runs of the same
digit and write "count + digit" for each run.
"""


def countAndSay(n: int) -> str:
    if n == 1:
        return "1"

    term = "1"
    for _ in range(n - 1):
        term = encode(term)
    return term


def encode(s: str) -> str:
    out = []
    curr = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == curr:
            count += 1
        else:
            # Digit changed: flush the current run.
            out.append(str(count) + curr)
            curr = s[i]
            count = 1
    # Flush the final run.
    out.append(str(count) + curr)

    return "".join(out)


"""
Walkthrough — n = 5

"1" -> "11" -> "21" -> "1211" -> "111221"

encode("1211"):
  i=1: '2'!='1' -> flush "11", curr='2', count=1
  i=2: '1'!='2' -> flush "12", curr='1', count=1
  i=3: '1'=='1' -> count=2
  after loop: flush "21"
  out: ["11", "12", "21"] -> "111221"

Time Complexity:  O(n * m) where m is the length of the nth term
Space Complexity: O(m) — one term stored at a time
"""
