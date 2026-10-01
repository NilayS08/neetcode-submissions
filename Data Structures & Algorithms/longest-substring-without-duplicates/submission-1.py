class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = set()
        l = 0
        max_length = 0

        for r in range(len(s)):
            while s[r] in subString:
                subString.remove(s[l])
                l += 1
            
            word_length = (r-l) + 1
            max_length = max(max_length, word_length)
            subString.add(s[r])
        return max_length
            
