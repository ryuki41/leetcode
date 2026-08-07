class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ["(", "{", "["]

        bracket_pair = {
            ")":"(",
            "}":"{",
            "]":"[" 
        }

        stack = []
        for c in s:
            if c in open_brackets:
                stack.append(c)
                continue
            
            if len(stack) == 0 or stack[-1] != bracket_pair[c]:
                return False
            
            stack.pop()
        
        return len(stack) == 0
