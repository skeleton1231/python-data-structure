from itertools import accumulate
from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        s = list(accumulate((-1 if v.isdigit() else 1 for v in array), initial=0))
        begin = end = 0
        first = {}
        for i , v in enumerate(s):
            j = first.get(v, -1)
            if j < 0:
                first[v] = i
            elif i - j > end - begin:
                begin, end = j, i
        return array[begin:end]