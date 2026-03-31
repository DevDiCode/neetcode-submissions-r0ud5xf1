class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        # Build frequency arrays
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        
        for ch in s1:
            s1_freq[ord(ch) - ord('a')] += 1
        
        k = len(s1)
        left = 0
        
        for right in range(len(s2)):
            # Add right character
            s2_freq[ord(s2[right]) - ord('a')] += 1
            
            # Maintain window size
            if right - left + 1 > k:
                s2_freq[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            # Compare arrays
            if right - left + 1 == k and s1_freq == s2_freq:
                return True
        
        return False