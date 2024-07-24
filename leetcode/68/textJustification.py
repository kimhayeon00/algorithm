class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cnt = 0
        answer = []
        lst = []
        tmp = []
        t = 0
        while True:
            i = words[t]
            if cnt + len(i) < maxWidth:
                if cnt > 0:
                    cnt += 1
                cnt += len(i) 
                tmp.append(i)

                if t == len(words)-1:
                    tmp.append(cnt)
                    lst.append(tmp)
                    break
                t += 1

            elif cnt + len(i) >= maxWidth:
                tmp.append(cnt)
                lst.append(tmp)
                tmp = []
                cnt = 0
            if t == len(words):
                break

        for word in lst:
            tmp_w = ""
            cnt = word[-1]
            width = 0
            cnt_al = len(word) - 2
            if cnt_al == 0:
                tmp_w += word[0]
                tmp_w += " " * (maxWidth - cnt)
            else:
                sub = (maxWidth - cnt) // cnt_al
                extra = (maxWidth - cnt) % cnt_al
                if word == lst[-1]:
                    for w in word[:-1]:
                        tmp_w += w
                        width+= len(w)
                        if width < maxWidth:
                            tmp_w += " "
                            width+= 1
                    if width < maxWidth:
                        tmp_w += " " * (maxWidth-width)
                else:
                    for w in word[:-1]:
                        # print(w, width)
                        tmp_w += w
                        width += len(w)
                        if width >= maxWidth:
                            break
                        tmp_w += " "
                        tmp_w += " " * sub
                        # print(tmp_w)
                        width += sub + 1
                        if extra:
                            tmp_w += " "
                            extra -= 1
                            width += 1
            answer.append(tmp_w)
        
        return answer

        
