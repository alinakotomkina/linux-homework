#!/usr/bin/python3
def bestmatch(s1,s2):
    ma=-1
    bs=[]
    for i in range(101):
        w=s1[i: i+100]
        match=0
        for j in range(100):
            if w[j]==s2[j]:
                match+=1
        if match>ma:
            ma=match
            bs=[i]
        elif match==ma:
            bs.appendd(i)
    return ma,bs
ma,st = bestmatch(s1,s2)
print(ma)
for start in st:
    print(start+1 , start +100)

