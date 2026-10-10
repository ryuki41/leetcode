class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur = {}

        for i, c in enumerate(s):
            last_occur[c] = i
        
        stack = []
        visited = set()
        for i, c in enumerate(s):
            if c in visited:
                continue

            while stack and c < stack[-1] and i < last_occur[stack[-1]]:
                visited.remove(stack.pop())
            
            stack.append(c)
            visited.add(c)
        
        return "".join(stack)


