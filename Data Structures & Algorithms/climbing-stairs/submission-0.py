class Solution:
    def climbStairs(self, n: int) -> int:

        def helper(n, lookup):

            if n in lookup:
                return lookup[n]

            if n <= 2:
                return n

            lookup[n] = helper(n - 1, lookup) + helper(n - 2, lookup)

            return lookup[n]

        return helper(n, {})
        