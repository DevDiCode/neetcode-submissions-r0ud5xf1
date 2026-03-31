class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()

        L = 0
        res = -sys.maxsize - 1

        for R in range(len(s)):

            while s[R] in lookup:
                lookup.remove(s[L])
                L += 1
            lookup.add(s[R])
            res = max(R - L + 1, res)
        return 0 if res == -sys.maxsize - 1 else res
