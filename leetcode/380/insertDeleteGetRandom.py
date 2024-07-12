import random
class RandomizedSet:

    def __init__(self):
        self.tmp = []

    def insert(self, val: int) -> bool:
        if val not in self.tmp:
            self.tmp.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.tmp: 
            self.tmp.remove(val)
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        return random.choice(self.tmp)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
