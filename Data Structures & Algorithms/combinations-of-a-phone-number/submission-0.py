class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # answer = []
        # number dictionary of number -> list of letters

        # backtrack(curr, index)
        # if index == len(digits):
        # answer.append(curr), return

        # for letter in dictionary[digits[index]]:
        # curr.append(letter)
        # backtrack(curr, index + 1)
        # curr.pop

        # backtrack([], 0)
        # return answer

        if digits == "":
            return []

        answer = []
        numbersDict = {"2": ["a", "b", "c"], 
                       "3": ["d","e","f"],
                       "4": ["g","h","i"],
                       "5": ["j","k","l"],
                       "6": ["m","n","o"],
                       "7": ["p","q","r","s"],
                       "8": ["t","u","v"],
                       "9": ["w","x","y","z"]}

        def backtrack(curr, index):
            if index == len(digits):
                answer.append("".join(curr[:]))
                return

            for letter in numbersDict[digits[index]]:
                curr.append(letter)
                backtrack(curr, index + 1)
                curr.pop()

        backtrack([], 0)
        return answer