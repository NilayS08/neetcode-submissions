class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""
        for i in strs:
            encoded_strs += str(len(i)) + "#" + i
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        res,i = [],0
        len_str = len(s)
        
        while i < len_str:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j+1+length
        return res