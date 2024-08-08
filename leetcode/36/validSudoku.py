class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tmp = [defaultdict(int) for _ in range(9)]
        spot = [defaultdict(int) for _ in range(9)] 
        for i in range(9):
            dic = defaultdict(int)
            for j in range(9):
                ri = i//3 
                rj = j//3
                r = ri+ri*2 + rj

                if board[i][j]!= ".":
                    dic[board[i][j]] += 1
                    spot[r][board[i][j]] += 1
                    if dic[board[i][j]] > 1:
                        # print(1, dic)
                        return False
                    if spot[r][board[i][j]] > 1:
                        # print(3, tmp)
                        return False
                if board[j][i] != ".":
                    tmp[i][board[j][i]] += 1
                    if tmp[i][board[j][i]] > 1:
                        # print(2, tmp)
                        return False
                
        # print(4, tmp)
        return True

        
        
        
