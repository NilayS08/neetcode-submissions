class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = set()
        l = 0
        maxLength = 0

        for r in range(len(s)):
            while s[r] in sub_string:
                sub_string.remove(s[l])
                l += 1
            w_len = (r-l) + 1
            maxLength = max(maxLength,w_len)
            sub_string.add(s[r])
        return maxLength