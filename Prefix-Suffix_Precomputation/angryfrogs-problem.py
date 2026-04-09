from typing import List

def solution(blocks: List[int]) -> int:
    n = len(blocks)
    if n == 1:
        return 1

    # left[i] is furthest left index reachable from i
    left = [0] * n
    for i in range(1, n):
        left[i] = left[i - 1] if blocks[i - 1] >= blocks[i] else i

    # right[i] is furthest right index reachable from i
    right = [0] * n
    right[n - 1] = n - 1
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] if blocks[i + 1] >= blocks[i] else i

    return max(right[i] - left[i] + 1 for i in range(n))

# Example test cases
test_blocks1 = [2, 6, 8, 5]
print(f"Max distance: {solution(test_blocks1)}") # answer should be 3

test_blocks2 = [1, 5, 5, 2, 6]
print(f"Max distance: {solution(test_blocks2)}") # answer should be 4

test_blocks3 = [1, 1]
print(f"Max distance: {solution(test_blocks3)}") # answer should be 2


