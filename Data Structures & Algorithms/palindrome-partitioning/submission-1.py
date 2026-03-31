class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(start, end):
            # Check if substring s[start..end] is palindrome
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def dfs(index, path):
            if index == len(s):
                res.append(path[:])
                return
            for i in range(index, len(s)):
                if isPalindrome(index, i):
                    path.append(s[index:i+1])
                    dfs(i+1, path)
                    path.pop()

        res = []
        dfs(0, [])
        return res