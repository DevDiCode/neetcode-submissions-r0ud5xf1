# ✅ Problem: Valid Palindrome II (Leetcode 680)
# Given a string s, return True if s can be a palindrome after deleting at most one character.

# ---------------------------------------------------------
# 🧠 Pattern: Two Pointers with At Most One Deletion
# Use a two-pointer scan; if a mismatch is found, try skipping either character and check if the substring is a palindrome.
# ---------------------------------------------------------

# 🔍 Step-by-Step Plan:
# 1. Preprocess: filter out non-alphanumeric, lowercase the string.
# 2. Use two pointers (L, R) from both ends.
# 3. On mismatch, check if either s[L+1:R+1] or s[L:R] is a palindrome (i.e., skip at most one character).
# 4. If no mismatch or one valid skip found, return True. Else, False.

# 🧪 Edge Cases:
# - Already a palindrome: return True.
# - Only one mismatch: check by skipping either char.
# - Empty string or single character: True.

# ⏱️ Time Complexity: O(n)
# 🔁 Space Complexity: O(n) for filtered string

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Step 1: Clean input (if required), Leetcode accepts raw strings (assume s is already alphanumeric/cased)
        def is_palindrome_range(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        L, R = 0, len(s) - 1
        while L < R:

            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                # Try removing s[L] or s[R]
                return is_palindrome_range(L+1, R) or is_palindrome_range(L, R-1)
        return True

# ✅ Example Test Cases
sol = Solution()
print(sol.validPalindrome("aba"))      # True
print(sol.validPalindrome("abca"))     # True ("b" removed)
print(sol.validPalindrome("abc"))      # False (need to remove 2 chars)
print(sol.validPalindrome("deeee"))    # True (remove 'd')
print(sol.validPalindrome("racecar"))  # True
