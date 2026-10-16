#!/usr/bin/python3
fl=1
k=0

while fl==1:
    dna=input()
    if dna=='STOP':
        fl=0
    fll=1
    for x in dna:
        if x not in 'ATGC' and fl==1:
            fll=0
            print("Неверная строка")
            break
    if fll==1 and fl==1:
        k+=1
print(k)

