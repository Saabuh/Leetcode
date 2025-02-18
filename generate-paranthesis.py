from typing import List

# the idea behind this question is that for every value n that we go through,
# we go through each valid parenthesis in the stack and create a new permutation
# of it by adding a new valid parenthesis "()" between each character. These then
# get added back to the stack and the process repeats.


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        my_set = set()

        stack.append("()")

        for i in range(1, n):

            while stack:

                p = stack.pop()

                for i in range(len(p)):
                    new_p = p[:i] + "()" + p[i:]

                    my_set.add(new_p)

            for p in my_set:
                stack.append(p)

            my_set.clear()

        return stack


solution = Solution()
print(solution.generateParenthesis(3))
