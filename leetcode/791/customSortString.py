class Solution:
        
    def customSortString(self, order: str, s: str) -> str:
        dic = {}
        etc = ""
        answer = ""
        for i in range(len(order)):
            dic[order[i]] = i
        
        for i in range(len(s)):
            if s[i] in dic :
                if len(answer) == 0:
                    answer = s[i]
                elif dic[answer[0]] >= dic[s[i]]:
                    answer = s[i] + answer
                elif dic[answer[-1]] < dic[s[i]]:
                    answer += s[i]
                else:
                    tmp = []
                    for char in answer:
                        tmp.append(dic[char])
                    findNum = dic[s[i]]
                    left = 0
                    right = len(tmp)-1

                    while left < right:
                        mid = (left + right)//2
                        if tmp[mid] == findNum:
                            answer = answer[:mid] + s[i] + answer[mid:]
                            break
                        elif tmp[mid] < findNum:
                            left = mid + 1
                        else:
                            right = mid
                    else:
                        answer = answer[:left] + s[i] + answer[left:]
            else:
                etc += s[i]
        return answer + etc
