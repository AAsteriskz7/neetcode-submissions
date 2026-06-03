class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        if s.lower() == s[::-1].lower():
            return True
        return False