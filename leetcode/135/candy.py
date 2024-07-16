class Solution:
    def candy(self, ratings: List[int]) -> int:
        lst = []
        for i in range(len(ratings)):
            if len(lst) > 0 and ratings[i-1] < ratings[i]:
                lst.append(lst[-1]+1)
            else:
                lst.append(1)

        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i] and lst[i-1] <= lst[i]:
                lst[i-1] = lst[i]+1

        return sum(lst)


        
