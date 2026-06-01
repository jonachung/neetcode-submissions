class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window to create the window for substring
        # set to keep track of characters.
        # if a character is already in the set
        # -> minimize the window
        # -> remove character of left pointer
        # -> increment left pointer + 1
        # else:
        # add character to set
        # get length of window and compare with answer (maxLength)
        # return maxLength

        answer = 0
        left = 0
        characterSet = set()

        for right in range(len(s)):

            while s[right] in characterSet:
                characterSet.remove(s[left])
                left += 1

            characterSet.add(s[right])
            answer = max(answer, right - left + 1)

        return answer