class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for num in range(n + 1):
            binaryNum = bin(num)
            answer.append(binaryNum.count('1'))

        return answer