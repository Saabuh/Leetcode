# https://leetcode.com/problems/encode-and-decode-strings
# idk

# pylint: disable=R


class Solution:

    def encode(self, strs: list[str]) -> str:

        encoded_str = " ".join(strs)

        return encoded_str

    def decode(self, s: str) -> list[str]:
        """decodes a string after being encoded with encode() function"""

        decoded_str = s.split(" ")

        return decoded_str


solution = Solution()
# print(f"encoded string: {solution.encode(["neet", "code", "love", "you"])}")
print(f"encoded string: {solution.encode([""])}")

# encoded_string = solution.encode(["neet", "code", "love", "you"])
encoded_string = solution.encode([""])
print(f"decoded string: {solution.decode(encoded_string)}")
