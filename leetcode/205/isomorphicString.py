class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST = {}
        mapTS = {}
        
        for i, j in zip(s, t):
            if (i in mapST and mapST[i] != j) or (j in mapTS and mapTS[j] != i)
                return False
            mapST[i] = j
            mapTS[j] = i
            
        return True
