#!/usr/bin/python3
import sys 
dna=sys.argv[1]
comp=dna.replace('C','1').replace("G","C").replace("1","G")
comp=dna.replace("A","2").replace("T","A").replace("2","T")
comp=comp[::-1]
rnk=dna.replace("T","U")
print(comp, rnk, dna.find("ATG"))


