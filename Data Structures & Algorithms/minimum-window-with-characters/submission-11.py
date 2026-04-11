class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        
        lookup = Counter(t)
        window ={}
        need = len(lookup)
        
        
        have = 0 
        L = min_start = 0 
        min_len = float("inf")
        


        for R, ch  in enumerate((s)):

            window[ch] = window.get(ch,0)+1

            if ch in lookup and window[ch]==lookup[ch]:
                have+=1
            


            while have == need:
                window_len = R - L + 1
                if window_len < min_len:
                    min_len = window_len
                    min_start = L

                
                left_char = s[L]

                window[left_char]-=1

                if left_char in lookup and window[left_char]<lookup[left_char]:
                    have-=1
                L+=1

        return "" if min_len == float("inf") else s[min_start:min_start + min_len]
 









