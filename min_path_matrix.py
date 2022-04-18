"""
Given a rectangular matrix, return the sum of the minimum path from leftmost column to the rightmost column.
Only 3 directions can move, right, up, down.

e.g.

[ [51 , 24 , 19*, 10* ],
[18*, 12*, 23*, 40 ],
[60 , 19 , 67 , 42 ]]

return 82
82=18+ 12+ 23+ 19+ 10

"""

grid = [[51, 24, 19, 10],
        [18, 12, 23, 40],
        [60, 19, 67, 42]]


def min_path(grid):
    return 0


print(min_path(grid))
