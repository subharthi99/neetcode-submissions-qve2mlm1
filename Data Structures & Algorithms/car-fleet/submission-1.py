class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pairs = [[p, s] for p, s in zip(position, speed)]
        pairs = sorted(zip(position, speed), reverse = True)
        fleets = 0
        cur_time = 0
        for p, s in pairs:
            t = (target - p)/s
            if t > cur_time:
                fleets += 1
                cur_time = t

        return fleets