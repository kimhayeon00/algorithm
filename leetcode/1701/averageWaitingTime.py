class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = 0
        total = 0
        for (i,j) in customers:
            if total < i:
                total = i
                total += j
                wait += total - i
            else:
                wait += total-i + j
                total += j

        return wait/len(customers)

