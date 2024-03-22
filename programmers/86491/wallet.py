def solution(sizes):
    row = []
    cul = []
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            row.append(sizes[i][0])
            cul.append(sizes[i][1])
        else:
            row.append(sizes[i][1])
            cul.append(sizes[i][0])
    
    return max(row) * max(cul)
