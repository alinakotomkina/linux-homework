#!/usr/bin/python3
seq=['AACG','AATG','TATG','TTTG']
n=len(seq)
matr=[]
for i in range(n):
    a=[]
    for j in range(n):
        k=0
        for c in range(len(seq[i])):
            if seq[i][c]!=seq[j][c]:
                k+=1
        a.append(k)
    matr.append(a)
for i in matr:
    print(' '.join(map(str,i)))


