class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_txt = ""
        for ch in s.lower():
            if ch.isalnum():
                clean_txt += ch
        
        text = "".join(clean_txt.split())
        textList = list(text)
            
        i = 0
        j = len(textList)-1
        while i < j:
            if textList[i] == textList[j]:
                i += 1
                j -= 1
            else:
                return False
        return True