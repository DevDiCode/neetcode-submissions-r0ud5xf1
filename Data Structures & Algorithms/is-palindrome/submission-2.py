class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = [ch.lower() for ch in s if ch.isalnum()]
        return check == check[::-1]