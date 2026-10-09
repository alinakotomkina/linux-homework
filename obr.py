#!/usr/bin/python3
dna=input()
dna=dna.replace("C","!").replace('G',"C").replace('!',"G")
dna=dna.replace("A",":").replace("T","A").replace(":","T")
print(dna[::-1])

