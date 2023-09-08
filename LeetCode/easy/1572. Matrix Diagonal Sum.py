class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        add = 0
        index = len(mat)
        for idx in range(index):
            add += mat[idx][idx]
            add += mat[idx][-idx-1]
        if index % 2 == 1: 
            add -= mat[(index // 2)][(index // 2)]
        return add