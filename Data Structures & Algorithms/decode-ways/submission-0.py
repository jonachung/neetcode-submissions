class Solution:
    def numDecodings(self, s: str) -> int:
        # dynamic programming

        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        if s[0] != "0":
            dp[1] = 1

        for i in range(2, len(s) + 1):
            if s[i - 1] != "0":
                dp[i] = dp[i - 1]

            twoDigitNumber = int(s[i - 2: i])
            if twoDigitNumber >= 10 and twoDigitNumber <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]