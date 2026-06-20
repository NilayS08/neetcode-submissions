class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []

        for i in range(n):
            distance_to_target = target - position[i]
            time_to_target = distance_to_target/speed[i]
            cars.append((position[i],time_to_target))
        cars.sort(reverse=True)
        stack = []

        for pos,time in cars:
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
        return len(stack)