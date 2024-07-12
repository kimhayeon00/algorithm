class RandomizedSet {
    private var lst : [Int] = []

    init() {}
    
    func insert(_ val: Int) -> Bool {
        if lst.contains(val) {
            return false
        }
        else{
            lst.append(val)
            return true
        }
    }
    
    func remove(_ val: Int) -> Bool {
        if let idx = lst.firstIndex(of: val) {
            lst.remove(at: idx)
            return true
        } else {
            return false
        }
    }
    
    func getRandom() -> Int {
        return lst.randomElement()!
        
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet()
 * let ret_1: Bool = obj.insert(val)
 * let ret_2: Bool = obj.remove(val)
 * let ret_3: Int = obj.getRandom()
 */
