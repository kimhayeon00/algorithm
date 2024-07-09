class Solution {
    func averageWaitingTime(_ customers: [[Int]]) -> Double {
        var wait = Int(0)
        var total = Int(0)

        for customer in customers{
            if total < customer[0]{
                total = customer[0] + customer[1]
                wait += total - customer[0]
            }
            else{
                wait += total-customer[0] + customer[1]
                total += customer[1]
            }
        }

        return Double(wait) / Double(customers.count)
    }
}
