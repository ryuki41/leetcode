class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur = {}
        for i in range(len(s)):
            last_occur[s[i]] = i
        
        stack = []
        seen = set()
        for i in range(len(s)):
            if s[i] in seen:
                continue
            
            while stack:
                if stack[-1] > s[i] and last_occur[stack[-1]] > i:
                    seen.remove(stack.pop())
                else:
                    break
            
            stack.append(s[i])
            seen.add(s[i])
        
        return "".join(stack)