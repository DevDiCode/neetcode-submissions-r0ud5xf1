class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Read length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            # Read the word of that length
            word = s[i:i+length]
            res.append(word)
            i = i + length
        return res
