class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        path = [p for p in path if p != ""]
        
        for p in path:
            if p == ".":
                continue
            
            if p == "..":
                if len(stack) >= 1:
                    stack.pop()
                continue
            
            stack.append(p)
        
        return "/" + "/".join(stack)