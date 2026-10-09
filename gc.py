#!/usr/bin/python3
k=0
dna=input()
for i in range(len(dna)):
    if dna[i]=="C" or dna[i]=="G":
        k+=1
pr=(k/len(dna))*100
print(f"{pr:.2f}")

