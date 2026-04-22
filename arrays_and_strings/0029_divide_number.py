'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
'''


class Solution(object):
    def divide(self, dividend, divisor):
        # Handle overflow case for the minimum 32-bit integer divided by -1.
        if dividend == -2**31 and divisor == -1:
            # Clamp to the maximum 32-bit signed integer value.
            return 2**31 - 1

        # Determine the sign of the final result.
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Work with absolute values to simplify the division logic.
        dividend = abs(dividend)
        divisor = abs(divisor)

        # Store the quotient here.
        result = 0

        # Keep subtracting the largest shifted divisor we can fit into dividend.
        while dividend >= divisor:
            # Start with the original divisor.
            temp = divisor
            # Track how many times the divisor has been doubled.
            multiple = 1

            # Double temp until it is too large to fit in the remaining dividend.
            while dividend >= (temp << 1):
                # Shift left to multiply temp by 2.
                temp <<= 1
                # Shift left to match the quotient contribution.
                multiple <<= 1

            # Remove the largest valid chunk from the dividend.
            dividend -= temp
            # Add the corresponding multiple to the result.
            result += multiple

        # Apply the sign to the final quotient.
        return sign * result


'''
Walkthrough Example

Input:
dividend = 10, divisor = 3

Step 1:
sign = 1
dividend = 10
divisor = 3

Step 2: First pass
temp = 3
multiple = 1

3 << 1 = 6, still <= 10
temp = 6
multiple = 2

6 << 1 = 12, now too large

Subtract:
dividend = 10 - 6 = 4
result = 2

Step 3: Second pass
temp = 3
multiple = 1

3 << 1 = 6, too large for dividend = 4

Subtract:
dividend = 4 - 3 = 1
result = 3

Step 4:
dividend < divisor, so stop

Final answer:
sign * result = 1 * 3 = 3

Time Complexity: O(log n)
Space Complexity: O(1)
'''
