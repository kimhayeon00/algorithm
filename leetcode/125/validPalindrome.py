class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        tmp = ""
        for i in s:
            if i.isalnum():
                tmp += i
                
        pre = 0
        last = len(tmp)-1
        while pre < last:
            if tmp[pre] != tmp[last]:
                return False
            else:
                pre += 1
                last -=1
        
        return True
        
