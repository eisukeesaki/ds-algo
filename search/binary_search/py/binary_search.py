from typing import List

class Search:
    @staticmethod
    def binary(x: int, space: List[int], lo: int, hi: int) -> int:
        while lo <= hi:
            """
            lo+(hi-lo) = search range
            """
            md = lo + (hi - lo) // 2

            if space[md] == x:
                return md
            elif space[md] < x:
                lo = md + 1
            else:
                hi = md - 1

        return -1

print(Search().binary(7, [0,1,2,3,4,5,6,7,8,9], 0, 10))

"""
l    m   h
0123456789
       x  
hi - lo = diff = range of search = num of elems in search scope
"""
