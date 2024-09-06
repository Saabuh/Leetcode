# https://leetcode.com/problems/top-k-frequent-elements
# 347

# pylint: disable=R

"""
first we need to add all the numbers to a hashmap/dictionary, where the K, V pair will be the unique value as the K and the # of occurences as the V.

(hashmaps work just like maps, in the sense where you have a key, value pairs stored in the map. The difference is that with a hashmap, operations such as 
insert, indexing, or removing only take O(1) time vs regular maps that index through the map, taking O(n).
it accomplishes this by hashing the value being stored/indexed/removed and matching the hashed value to a corresponding unique index in the map, making the operation take O(1) time vs 
going through each index to find the corresponding index.)

after populating the freq_dict, we need to sort it based on the value. We can do so by using the sorted() function, utilizing the key parameter.
the iterable will be the freq_dict.items(), which is a list of (K, V) tuples.
the key allows us to pass a function that will be called on every element in the iterable, using the function's result/return to compare for sorting instead
of the default that the sorted() function goes to.
then we sort by descending order using the reverse parameter.

finally we go through the first k elements in the sorted_dict, returning it as a list of the top k elements.
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        freq_dict = {}

        # count occurrences for each unique value, store as V with K = unique value
        for num in nums:
            if num in freq_dict:
                freq_dict[num] = freq_dict[num] + 1
            else:
                freq_dict[num] = 1

        # sort based on value = # of occurences of each unique value
        sorted_dict = dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))

        # top k elements list
        k_list = []

        for index, key in enumerate(sorted_dict.keys()):
            if index < k:
                k_list.append(key)

        return k_list


solution = Solution()
print(solution.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
