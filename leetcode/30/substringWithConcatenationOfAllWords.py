class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words[0])
        lenWord = len(words)
        substr = n * lenWord
        answer = []
        word_count = defaultdict(int)

        for word in words:
            word_count[word] += 1

        if "".join(words) == s:
            return [0]
    
        for i in range(len(s)-substr+1):
            seen = defaultdict(int)
            start = i
            for j in range(lenWord):
                tmp = s[start:start+n]
                if tmp in words:
                    seen[tmp] += 1
                else:
                    break
                
                if seen[tmp] > word_count[tmp]:
                    break
                start += n
            if seen == word_count:
                answer.append(i)
        return answer
        

        
