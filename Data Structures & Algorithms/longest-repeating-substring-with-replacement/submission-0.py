class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # add string to set to get # of unique characters
        # for each char, do sliding window to keep track of substring
        # can have up to k characters that are not letter
        # if exceed k -> update window by moving left pointer until does
        # not exceed k

        charSet = set(s)
        answer = 0

        for char in charSet:
            left = 0
            count = 0
            for right in range(len(s)):
                if s[right] == char:
                    count += 1

                while (right - left + 1 - count > k):
                    if s[left] == char:
                        count -= 1
                    left += 1

                answer = max(answer, right - left + 1)

        return answer