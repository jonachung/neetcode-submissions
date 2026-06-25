class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # take (position, speed) pairs and sort in reverse order so
        # first element in pair list is closest to target
        # define stack
        # for each car, computer time take to reach target and push to stack
        # if a new car's time <= time in stack, do not add to stack

        # len of stack is answer
        stack = []
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        pairs.sort(reverse=True)
        stack.append((target - pairs[0][0]) / pairs[0][1])

        for i in range(1, len(pairs)):
            position, speed = pairs[i]
            time = (target - position) / speed
            if time > stack[-1]:
                stack.append(time)

        return len(stack)