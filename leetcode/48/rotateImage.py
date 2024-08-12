class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        tmp = deepcopy(matrix)
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                matrix[i][j] = tmp[n-1-j][i]
