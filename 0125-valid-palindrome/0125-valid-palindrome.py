class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([s_.lower() for s_ in s if s_.isalpha() or s_.isdigit()])
        half = len(s)//2
        prev, post = s[:half], s[half:][::-1]
        return prev == post if len(prev) == len(post) else s[:half] == s[half:][::-1][:-1]