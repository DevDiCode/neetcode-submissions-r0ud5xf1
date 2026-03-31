from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        lookup = Counter(t)
        required = len(lookup)
        have = 0

        left = 0
        res_len = float("inf")
        res_start = 0

        for right in range(len(s)):
            char = s[right]
            if char in lookup:
                lookup[char] -= 1
                if lookup[char] == 0:
                    have += 1

            # Shrink window if all characters are matched
            while have == required:
                window_len = right - left + 1
                if window_len < res_len:
                    res_len = window_len
                    res_start = left

                # Remove the leftmost character
                if s[left] in lookup:
                    lookup[s[left]] += 1
                    if lookup[s[left]] > 0:
                        have -= 1
                left += 1

        if res_len == float("inf"):
            return ""
        return s[res_start:res_start + res_len]
