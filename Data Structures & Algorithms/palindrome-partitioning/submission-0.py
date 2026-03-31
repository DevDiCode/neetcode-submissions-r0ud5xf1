
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res: List[List[str]] = []
        n = len(s)

        def is_palindrome(l: int, r: int) -> bool:
            # Two-pointer palindrome check (correct)
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(start: int, path: List[str]) -> None:
            if start == n:
                res.append(path.copy())
                return
            for end in range(start, n):
                if is_palindrome(start, end):
                    path.append(s[start:end+1])
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return res