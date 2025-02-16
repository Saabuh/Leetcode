from collections import deque


class Solution:
    # def isValid(self, s: str) -> bool:
    #
    #     stack = deque()
    #     # closeToOpen = {"]": "[", ")": "(", "}": "{"}
    #
    #     if len(s) % 2 == 1:
    #         return False
    #
    #     for c in s:
    #         if c == "(" or c == "[" or c == "{":
    #             stack.append(c)
    #         else:
    #             if len(stack) == 0:
    #                 return False
    #
    #             value = stack.pop()
    #             if c == ")" and value != "(":
    #                 return False
    #             elif c == "]" and value != "[":
    #                 return False
    #             elif c == "}" and value != "{":
    #                 return False
    #
    #     if len(stack) > 0:
    #         return False
    #
    #     return True

    def isValid(self, s: str) -> bool:

        stack = deque()
        closeToOpen = {"]": "[", ")": "(", "}": "{"}

        for c in s:

            ## check if c is a closing brace
            if c in closeToOpen:
                ##check stack non empty and next open brace corresponds to its closing brace
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        ## check if stack is empty or not
        return not bool(stack)


solution = Solution()
print(solution.isValid("[](){}"))
