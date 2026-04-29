class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_Str = ''

        for c in s:
            if c.isalnum():
                new_Str += c.lower()
        return new_Str == new_Str[::-1]