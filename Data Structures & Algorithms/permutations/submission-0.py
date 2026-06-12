class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking with curr (curr permutation being made, current array to traverse)
        # if len(curr) == len(nums) -> answer.append(curr[:]) return
        # for j in range(i, len(array))
        # curr.append(array[j])
        # backtrack(curr, array[:j] + array[j+1:]) -> basically take out index j from array
        # curr.pop()
        answer = []

        def backtrack(curr, array):
            if len(curr) == len(nums):
                answer.append(curr[:])
                return

            for j in range(len(array)):
                curr.append(array[j])
                backtrack(curr, array[:j]+array[j+1:])
                curr.pop()

        backtrack([], nums)
        return answer