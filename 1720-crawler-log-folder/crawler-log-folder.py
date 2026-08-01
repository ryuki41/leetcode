class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # どれくらいの深さのディレクトリを開いているか
        folder_stack = []

        for log in logs:
            if log == "../":
                if len(folder_stack) == 0:
                    continue
                else:
                    folder_stack.pop()
            elif log == "./":
                continue
            else:
                folder_stack.append(log)
        
        return len(folder_stack)

        