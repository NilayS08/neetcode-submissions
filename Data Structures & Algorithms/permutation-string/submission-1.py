class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w_s1 = len(s1)
        freq_s1 = Counter(s1)
        w_s2 = ""

        if len(s1) > len(s2):
            return False
        
        for i in range(w_s1):
            w_s2 += s2[i]
            freq_s2 = Counter(w_s2)
            if freq_s1 == freq_s2:
                return True
        for right in range(w_s1, len(s2)):
            w_s2 = w_s2[1:] + s2[right]
            
            freq_s2 = Counter(w_s2)
            
            if freq_s1 == freq_s2:
                return True
        return False