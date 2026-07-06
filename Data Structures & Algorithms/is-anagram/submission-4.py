# Manual hash map counting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap_s = {}
        hashMap_t = {}

        for char in s:
            hashMap_s[char] = hashMap_s.get(char, 0) + 1
        
        for char in t:
            hashMap_t[char] = hashMap_t.get(char, 0) + 1
        
        if hashMap_s == hashMap_t:
            return True
        else:
            return False
        