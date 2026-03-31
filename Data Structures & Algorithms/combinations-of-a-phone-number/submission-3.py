# Letter Combinations of a Phone Number (LeetCode 17)
# ---------------------------------------------------
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations
# that the number could represent, based on the telephone keypad mapping.

from typing import List

# 1) Exploration:
# - Each digit maps to 3-4 letters (e.g., '2' -> 'abc', '7' -> 'pqrs').
# - We need all combinations by choosing one letter per digit in order.
# - If digits == "" -> return [] (no combinations).

# 2) Brainstorm:
# A) Backtracking (chosen)
#    - Depth equals number of digits.
#    - At each position, try all letters mapped to the current digit.
#    - When index == len(digits), push built string to result.
#
# B) Iterative BFS-style building
#    - Start with [""] and iteratively append letters for each digit.
#
# Both are fine; backtracking is clear and idiomatic.

# 3) Plan (Backtracking):
# - Map each digit to its letters.
# - helper(index, path):
#     - If index == len(digits): add joined path to result.
#     - Else: for each letter in mapping[digits[index]]:
#         - Append letter, recurse to index+1, then pop.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        res: List[str] = []
        path: List[str] = []

        def helper(index: int) -> None:
            if index == len(digits):
                res.append("".join(path))
                return
            for ch in digit_to_char[digits[index]]:
                path.append(ch)
                helper(index + 1)
                path.pop()

        helper(0)
        return res

# 4) Edge Cases:
# - "" -> []
# - "2" -> ["a","b","c"]
# - Long input (up to 4 digits typically in interviews) -> 3^n to 4^n combinations

# 5) Complexity:
# - Let k be average branching factor (~3.25), n = len(digits).
# - Time: O(k^n * n) due to building strings (join cost up to O(n) each)
# - Space: O(n) recursion depth + O(k^n) output

# 6) Iterative alternative (optional):
def letter_combinations_iterative(digits: str) -> List[str]:
    if not digits:
        return []
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    res = [""]
    for d in digits:
        next_res = []
        for prefix in res:
            for ch in mapping[d]:
                next_res.append(prefix + ch)
        res = next_res
    return res

# 7) Tests (commented):
# print(Solution().letterCombinations("23"))
# # Expected (order may vary): ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# print(Solution().letterCombinations(""))     # []
# print(Solution().letterCombinations("7"))    # ["p","q","r","s"]
