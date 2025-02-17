from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                result = 0

                match token:
                    case "+":
                        result = num1 + num2
                    case "-":
                        result = num1 - num2
                    case "*":
                        result = num1 * num2
                    case "/":
                        result = int(num1 / num2)

                stack.append(str(result))

            else:
                stack.append(token)

        return int(stack.pop())


solution = Solution()
# solution.evalRPN(["2", "1", "+", "3", "*"])
# solution.evalRPN(["4", "13", "5", "/", "+"])
print(
    solution.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)
