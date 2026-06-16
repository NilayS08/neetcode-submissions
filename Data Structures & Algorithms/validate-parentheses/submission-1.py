class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        par_map = {')':'(', '}':'{',']':'['}
        stack  = []
            
        for c in s:
            if c in par_map:
                if stack and stack[-1] == par_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
