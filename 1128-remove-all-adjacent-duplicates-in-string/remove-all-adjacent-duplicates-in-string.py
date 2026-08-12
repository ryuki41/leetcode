class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for c in s:
            stack.append(c)
            
            while len(stack) >= 2:
                if stack[-1] == stack[-2]:
                    for _ in range(2):
                        stack.pop()
                else:
                    break
            
        
        return "".join(stack)
                