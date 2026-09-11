class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pair = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        close_brackets = [")", "}", "]"]

        stack = []

        for bracket in s:
            if not stack:
                stack.append(bracket)
                continue
            
            if bracket in close_brackets and stack[-1] == bracket_pair[bracket]:
                stack.pop()
                continue
            
            stack.append(bracket)
            
        return len(stack) == 0
