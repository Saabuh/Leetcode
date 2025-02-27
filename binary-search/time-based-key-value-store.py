# the key idea here is that we can have a dictionary storing each unique person as a key, and a timestamp of all their
# reactions in a list["sad", 2]. we can just append it to the end of each persons list because we know that the set calls
# will always be in inreasing order, so our lists will be sorted by default. Then, we just perform a binary search on
# the timestamps.
# One caveat is that the timestamps we want has to be the latest timestamp of their reaction that is still less than or
# equal to the timestamp that they provide. So if t = 5, but timestamp reaction 5 doesnt exists, return 4. If that doesnt
# exist, return 3, etc. So our search property is that given timestamp t, we have  prev < T <= t, where prev
# is the previous found timestamp. and T is the current timestamp we're searching.


class TimeMap:

    def __init__(self):
        self.my_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.my_dict:
            self.my_dict[key].append([value, timestamp])
        else:
            self.my_dict[key] = []
            self.my_dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        if key in self.my_dict:
            timestamps = self.my_dict[key]
        else:
            return ""
        # print(timestamps)

        l, r = 0, len(timestamps) - 1
        res = ["", -1]

        while l <= r:

            mid = l + (r - l) // 2
            # print(mid)
            # print(timestamps[l : r + 1])

            if timestamps[mid][1] <= timestamp and timestamps[mid][1] > res[1]:
                res = timestamps[mid]
                l = mid + 1
                # print(l, r)
            else:
                r = mid - 1
                # print(l, r)

        return res[0]


timeMap = TimeMap()
timeMap.set("alice", "happy", 1)
timeMap.set("alice", "sad", 3)
timeMap.set("alice", "mad", 4)
timeMap.set("alice", "sad", 5)
timeMap.set("alice", "happy", 7)
# print(timeMap.get("alice", 1))
# print(timeMap.get("alice", 2))
# print(timeMap.get("alice", 3))
print(timeMap.get("alice", 6))
# print(timeMap.my_dict)
