class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_dict = {
            "}": "{",
            "]":"[",
            ")":"("
        }

        for i in s:
            if i in map_dict.values():
                stack.append(i)
            elif len(stack) > 0 and map_dict[i] == stack[-1] :
                stack.pop()
            else:
                return False
            
        return True if not stack else False