class Solution:
    def checkValidString(self, s: str) -> bool:
        # greedy algorithm to figure out the min/max number of '(' that COULD be open
        # '(' -> always increase numbers
        # ')' -> always descrease numbers
        # '*' -> flexible and can decrease open count or increase open count or don't do either ('(' or ')' or empty)
        # if leftMax is negative -> invalid
        # at end, if leftMin is 0, then string is Valid

        leftMin = 0
        leftMax = 0

        for character in s:
            if character == '(':
                leftMin += 1
                leftMax += 1
            elif character == ')':
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1

            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0 # treat extra * as empty

        if leftMin == 0:
            return True
        return False

