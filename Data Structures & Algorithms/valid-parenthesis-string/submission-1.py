class Solution:
    def checkValidString(self, s: str) -> bool:
        # 2 stacks for left and star
        # append to the stack
        # if right ) -> pop from left stack first if nothing, then use star
        #            -> before, check if both are empty, if so then return false

        # if left and star still have elements left.
        # if index in left.pop greater than index in star.pop -> '*(' and this is invalid so retur False
        # return true if left is empty, else return false
        left = []
        star = []
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if len(left) == 0 and len(star) == 0:
                    return False
                if len(left) > 0:
                    left.pop()
                else:
                    star.pop()

        while len(left) > 0 and len(star) > 0:
            if left.pop() > star.pop():
                return False

        if len(left) == 0:
            return True
        return False

