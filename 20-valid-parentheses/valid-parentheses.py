class Solution:
    def isValid(self, s: str) -> bool:
        # 開きカッコをスタックしていく
        bracket_stack = []
        open_brackets = ["(", "{", "["]
        bracket_pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for bracket in s:
            if bracket in open_brackets:
                bracket_stack.append(bracket)
            else:
                if not bracket_stack or bracket_stack[-1] != bracket_pairs[bracket]:
                    return False
                bracket_stack.pop()

        return len(bracket_stack) == 0