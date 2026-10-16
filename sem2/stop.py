#!/usr/bin/python3
rna=input()
k=0
for i in range(0,len(rna),3):
    if rna[i:i+3]=="UAA" or rna[i:i+3]=='UAG' or rna[i:i+3]=='UGA':
        st=rna[i:i+3]
        break
    else:
        k+=1
print('Количество кодирующих кодонов:',k)
print("Стоп-кодон:",st)



