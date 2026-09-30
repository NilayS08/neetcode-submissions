class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s if self.isAlphaNumeric(char)]).lower()
        l, r = 0, len(s) - 1
        while l < r :
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

    
    def isAlphaNumeric(self,s):
        if ord("a") <= ord(s) <= ord("z"):
            return True
        if ord("A") <= ord(s) <= ord("Z"):
            return True
        if ord("0") <= ord(s) <= ord("9"):
            return True
        else:
            return False