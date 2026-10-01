class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        t_freq, window = {}, {}

        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1
        
        have = 0
        need = len(t_freq)

        res = [-1,-1]
        res_len = float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in t_freq and window[c] == t_freq[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < res_len:
                    res = [l,r]
                    res_len = (r-l+1)
                window[s[l]] -= 1

                if s[l] in t_freq and window[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l:r+1] if res_len != float("infinity") else ""