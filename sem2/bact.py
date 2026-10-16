#!/usr/bin/python3
growth=[[0,2,4,8],[0,1,1,2],[0,3,6,9]]
p=5
for x in growth:
    fl=0
    for i,value in enumerate(x):
        if value>=5:
            print(i)
            fl=1
            break
    if fl==0:
        print("Отсутствует")


