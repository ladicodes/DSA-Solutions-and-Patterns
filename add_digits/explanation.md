## AddDigit
This was one of the questions that I got during my recent interview,
The problem was to write an algorithm in which the individual digits of an integer are summed up. The integer in this case can be positive or negative. E.g
123 => 1+ 2+ 3 = 6
-2048 => -2 + 0 + 4 + 8 = 10

## Core Idea
You repeatedly extract the last digit of the number and add it to a running sum until the number is exhausted.

## How digit extraction works
In Go:
n % 10  gives the last digit of n
n / 10  removes the last digit (integer division truncates decimals)
Example:
123 % 10 = 3
123 / 10 = 12
## Complexity
-Time: O(d) (linear in number of digits)
-Space: O(1) (constant extra memory)
## Algorithm
Positive numbers (n > 0)
-Initialize sum = 0
-While n > 0:
 Add last digit to sum: sum += n % 10
 Remove last digit: n = n / 10
-Return sum

Negative numbers (n < 0)
-Convert number to positive: n = -n
-Initialize temp = n, sum = 0
Then:
-Extract digits using the same rule:
 sum += temp % 10
 temp = temp / 10
-Extract first digit:
-Keep dividing n by 10 until n < 10
-Apply final rule:
Return sum - (2 × firstDigit)

## Termination Condition
The loop stops when n == 0 because repeated integer division eventually reduces any positive integer to zero.

## Final comments
Why we return sum - (2 × firstDigit)

After converting the number to positive and getting the sum, we have two things:

sum => sum of all digits
firstDigit => the most significant digit (leftmost digit)

The negative-number rule applies an adjustment to the normal digit sum.

Let’s use an example:

-2048
Step 1: Work with the absolute value
2048
Step 2: Get the digit sum
2 + 0 + 4 + 8 = 14
sum = 14
Step 3: Extract first digit
2048 → 2
firstDigit = 2
Step 4: Apply the rule
result = sum - (2 × firstDigit)

So:
result = 14 - (2 × 2)
       = 14 - 4
       = 10