class Solution {
    func candy(_ ratings: [Int]) -> Int {
        var lst : [Int] = [1]

        for i in 1..<ratings.count{
            if ratings[i-1] < ratings[i]{
                lst.append(lst[i-1]+1)
            }
            else{
                lst.append(1)
            }
        }

        for i in stride(from: ratings.count-1, through: 1, by: -1){
            if ratings[i-1] > ratings[i] && lst[i-1] <= lst[i]{
                lst[i-1] = lst[i]+1
            }
        }
        return lst.reduce(0,+)
    }
}
