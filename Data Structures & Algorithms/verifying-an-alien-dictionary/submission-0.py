from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {ch: i for i, ch in enumerate(order)}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            # Prefix rule: longer word before its prefix is NOT valid!
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return False
            for j in range(min_len):
                if w1[j] != w2[j]:
                    # Return False if order is wrong according to alien language
                    if rank[w1[j]] > rank[w2[j]]:
                        return False
                    break
        return True
