class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) means u can only look at number once
        # put nums in a set
        # answer for running length, answer = 0
        # for loop to find number where number - 1 is not in the set
        # start = num
        # while (start + 1) in set -> length += 1, start +=1
        # answer = max(answer, length)

        answer = 0
        numSet = set(nums)

        for num in numSet:
            if (num - 1) not in numSet:
                start = num
                length = 1
                while (start + 1) in numSet:
                    length += 1
                    start += 1
                answer = max(answer, length)

        return answer