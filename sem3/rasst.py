#!/usr/bin/python3
dna1=input()
dna2=input()
def f(dna):
    alf='ATCG'
    if len(dna)>0:
        for x in dna:
            if x not in alf:
                   return 0
        return 1
    else:
        return 0
def is_valid_dna(dna1,dna2):
    if f(dna1)==1 and f(dna2)==1:
        return True
    return False

def hamming_distance(s1,s2):
    if len(s1)==len(s2) and is_valid_dna(s1,s2):
        k=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                k+=1
        return k
    return None




print(is_valid_dna(dna1,dna2))
print(hamming_distance(dna1,dna2))





