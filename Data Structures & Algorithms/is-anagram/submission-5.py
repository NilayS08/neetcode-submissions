# Manual hash map counting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        for c in s:
            hash_s[c] = hash_s.get(c, 0) + 1
        for c in t:
            hash_t[c] = hash_t.get(c, 0) + 1
        
        if hash_s == hash_t:
            return True
        else:
            return False