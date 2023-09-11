from typing import List # import to make editor stop crying at me

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = dict()
        result = []
        for i, size in enumerate(groupSizes):
            if size not in group:
                group[size] = []
            group[size].append(i)

            if len(group[size]) == size:
                result.append(group[size])
                group[size] = []
        return result