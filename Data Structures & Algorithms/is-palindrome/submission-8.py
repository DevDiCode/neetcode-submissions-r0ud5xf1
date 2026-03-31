# ✅ Problem: Valid Palindrome (Leetcode 125)
# Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# ---------------------------------------------------------
# 🧠 Pattern: Two Pointers
# Clean the input string to include only lowercase alphanumeric characters,
# then use two pointers to compare characters from both ends.
# ---------------------------------------------------------

# 🔍 Step-by-Step Plan:
# 1. Filter the string to include only lowercase alphanumeric characters.
# 2. Use two pointers (L, R) starting from both ends.
# 3. Move toward the center while comparing characters.
# 4. If mismatch found, return False.
# 5. If pointers cross, return True.

# 🧪 Edge Cases:
# - Empty string → True (a valid palindrome).
# - All non-alphanumeric → True.
# - Mixed case letters → should be considered equal.
# - Single character → True.

# ⏱️ Time Complexity: O(n) – one pass for filtering + one pass for checking
# 🔁 Space Complexity: O(n) – to store the filtered string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Filter and lowercase alphanumeric characters
        filtered = [ch.lower() for ch in s if ch.isalnum()]

        # Step 2: Two pointer comparison
        L, R = 0, len(filtered) - 1
        while L < R:
            if filtered[L] != filtered[R]:
                return False
            L += 1
            R -= 1

        return True


# ✅ Example Test Cases
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(sol.isPalindrome("race a car"))  # False
print(sol.isPalindrome(""))  # True
