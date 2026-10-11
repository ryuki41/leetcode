class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur = {}
        for i in range(len(s)):
            last_occur[s[i]] = i
        
        left = 0
        stack = []
        seen = set()
        print(last_occur)

        for i in range(len(s)):
            if s[i] in seen:
                continue

            while stack:
                if stack[-1] > s[i] and last_occur[stack[-1]] > i:
                    seen.remove(stack[-1])
                    stack.pop()
                else:
                    break
        
            stack.append(s[i])
            seen.add(s[i])

        
        return "".join(stack)