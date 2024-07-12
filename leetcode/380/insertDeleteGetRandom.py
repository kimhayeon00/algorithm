import random
class RandomizedSet:

    def __init__(self):
        self.tmp = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.dic[val] = len(self.tmp)
            self.tmp.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dic:
            idx = self.dic[val]
            self.tmp[idx] = self.tmp[-1]
            self.dic[self.tmp[-1]] = idx
            self.tmp.pop()
            del self.dic[val]
            
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
