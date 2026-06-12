class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = set()
        candidates.sort()

        def backtrack(curr, currSum, i):
            if currSum == target:
                answer.add(tuple(curr))
                return

            if i == len(candidates) or currSum > target:
                return

            curr.append(candidates[i])
            backtrack(curr, currSum + candidates[i], i + 1)
            curr.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1 # skip duplicates

            backtrack(curr, currSum, i + 1)

        backtrack([], 0, 0)
        return [list(combination) for combination in answer]