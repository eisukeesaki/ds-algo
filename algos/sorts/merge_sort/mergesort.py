from typing import List

class Sort():
    def merge(space: List[int], lo: int, hi: int) -> List[int]:
        pass
        
sort = Sort()
nums = [5,1,9,8,2,7,4,3,6,0]
print(sort.merge(nums))

"""
task: sort list of ints in asc order

                     2,6,8,2,3,9,1,4,9            
----------------------------------------------------------divide
          2,6,8,2,3                    9,1,4,9
     2,6,8         2,3            9,1,4         9
  2,6     8       2   3        9,1     4       9   
 2   6                        9   1
----------------------------------------------------------compare & combine
  2,6       2,8         3,9         1,4        9
     2,2,6,8                 1,3,4,9           9
----------------------------------------------------------
                     1,2,2,3,4,6,8,9,9

f mergesort(space, l, h) -> sorted_space
    tasks
        divide
            recursive call
                stop condition
                    space has 1 element
                op
                    halve range
        compare
            order
                less,great
        combine
    
---
https://developer.nvidia.com/blog/merge-sort-explained-a-data-scientists-algorithm-guide/
"""
