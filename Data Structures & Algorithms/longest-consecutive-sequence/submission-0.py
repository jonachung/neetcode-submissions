class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put the numbers in a set
        # loop through the numbers in set
        # if number - 1 not in the set:
        #   make that number as "start"
        #   check if start + 1 is in set
        #.      if so then increment start and increment sequenceLength
        #   update sequence legnth accordingly 

        numSet = set(nums)
        answer = 0

        for num in numSet:
            if (num - 1) not in numSet:
                start = num
                sequenceLength = 1
                while (start + 1) in numSet:
                    start += 1
                    sequenceLength += 1
                answer = max(sequenceLength, answer)


        return answer