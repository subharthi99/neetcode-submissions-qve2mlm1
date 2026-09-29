class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # store key: list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            mid = l + (r - l)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res
