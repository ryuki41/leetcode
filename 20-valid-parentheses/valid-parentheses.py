class Solution:
    def isValid(self, s: str) -> bool:
        # 各開きカッコの数をカウントする
        count_stack = []

        for char in s:
            match char:
                case "(" | "{" | "[":
                    count_stack.append(char)
                case ")":
                    if not count_stack or count_stack[-1] != "(":
                        return False
                    else:
                        count_stack.pop()
                case "}":
                    if not count_stack or count_stack[-1] != "{":
                        return False
                    else:
                        count_stack.pop()
                case "]":
                    if not count_stack or count_stack[-1] != "[":
                        return False
                    else:
                        count_stack.pop()

        return len(count_stack) == 0