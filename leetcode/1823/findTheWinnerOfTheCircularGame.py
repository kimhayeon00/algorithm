class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst = [i for i in range(1, n+1)]
        start = 0

        while len(lst) > 1:
            idx = (start + k -1) % len(lst) 
            lst.remove(lst[idx])

            start = idx % n

        return lst[0]
