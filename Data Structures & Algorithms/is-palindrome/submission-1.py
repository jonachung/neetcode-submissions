class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        left = 0
        right = len(s) - 1
        while (left < right):
            if s[left] in alphanumeric and s[right] in alphanumeric:
                # do stuff
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
            else:
                if s[left] not in alphanumeric:
                    left += 1
                if s[right] not in alphanumeric:
                    right -= 1

        return True
                
            