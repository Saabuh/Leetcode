from typing import List

# this question is insane
# the key idea behind this question is that the cars cannot pass eachother, so it could be thought of as a one way lane.
# in that case, we look at the cars positions in descending order, because we want to see if the car at the front will form
# a fleet or not.
# another note, if a car forms a fleet, it will never catch up to the fleet in "front" of it, because if it didnt catch up
# it wasnt a fleet, it definitely won't catch up when it forms its own fleet and slows down.
# another aside, imagine a car catching up to a fleet and then disappearing, because it will end up matching the speed and
# position of the car ahead of it, so no information is really needed from it anymore.


class Solution:
    # def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    #
    #     # map positions to speed
    #     fleets = []
    #     sorted_list = []
    #     prev_car = []
    #     count = 1
    #
    #     for i in range(len(position)):
    #         sorted_list.append([position[i], speed[i]])
    #
    #     sorted_list = sorted(sorted_list, reverse=True)
    #
    #     for car in sorted_list:
    #
    #         if not fleets:
    #             fleets.append(car)
    #             prev_car = car
    #             continue
    #
    #         car_time = float(target - car[0]) / car[1]
    #         prev_car_time = float(target - prev_car[0]) / prev_car[1]
    #
    #         if prev_car_time > car_time:
    #             fleets[-1][1] = min(fleets[-1][1], car[1])
    #         else:
    #             fleets.append(car)
    #
    #         prev_car = car
    #
    #     print(fleets)

    # def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    #
    #     fleets = []
    #     sorted_list = []
    #
    #     for i in range(len(position)):
    #         sorted_list.append([position[i], speed[i]])
    #
    #     sorted_list = sorted(sorted_list, reverse=True)
    #
    #     for i, car in enumerate(sorted_list):
    #
    #         if i == 0:
    #             fleets.append(car)
    #             continue
    #
    #         car_time = float(target - car[0]) / car[1]
    #         ahead_car_time = float(target - fleets[-1][0]) / fleets[-1][1]
    #
    #         if car_time <= ahead_car_time:
    #             fleets[-1][1] = min(fleets[-1][1], car[1])
    #         else:
    #             fleets.append(car)
    #
    #     return len(fleets)

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleets = 1
        sorted_list = []

        for i in range(len(position)):
            sorted_list.append([position[i], speed[i]])

        sorted_list = sorted(sorted_list, reverse=True)

        ahead_car_time = (target - sorted_list[0][0]) / sorted_list[0][1]

        for i in range(1, len(sorted_list)):

            car_time = float(target - sorted_list[i][0]) / sorted_list[i][1]

            if car_time > ahead_car_time:
                fleets += 1
                ahead_car_time = car_time

        return fleets


solution = Solution()

print(solution.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
