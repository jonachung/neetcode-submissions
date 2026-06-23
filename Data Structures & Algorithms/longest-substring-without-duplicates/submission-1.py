class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window to find substring with no dup characters
        # keep global variable to keep track of longest substring length
        # have a set to keep track of characters
        # while a character is in set -> set.remove(s[left]) left += 1
        # add s[right] to set
        # get length of window and compare to global variable

        answer = 0
        characterSet = set()

        left = 0
        for right in range(len(s)):
            while s[right] in characterSet:
                characterSet.remove(s[left])
                left += 1
            
            characterSet.add(s[right])
            answer = max(answer, right - left + 1)

        return answer