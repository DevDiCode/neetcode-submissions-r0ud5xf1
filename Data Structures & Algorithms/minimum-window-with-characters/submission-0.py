from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        ref_lookup = Counter(t)
        curr_lookup = {}
        have, need = 0, len(ref_lookup)
        res = [float("inf"), None, None]
        L = 0

        for R in range(len(s)):
            c = s[R]
            curr_lookup[c] = curr_lookup.get(c, 0) + 1

            if c in ref_lookup and curr_lookup[c] == ref_lookup[c]:
                have += 1

            while have == need:
                # Update result if window is smaller
                if (R - L + 1) < res[0]:
                    res = [R - L + 1, L, R]

                # Shrink from the left
                curr_lookup[s[L]] -= 1
                if s[L] in ref_lookup and curr_lookup[s[L]] < ref_lookup[s[L]]:
                    have -= 1
                L += 1

        l, r = res[1], res[2]
        return s[l:r+1] if res[0] != float("inf") else ""
