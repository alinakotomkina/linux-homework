#!/usr/bin/python3
def f(n):
    f=[]
    with open(n,'r') as file:
        for line in file:
            line=line.strip()
            if line.startswith('>'):
                f.append({'metadata':line[1:], 'data':''})
            else:
                f[-1]['data']+=line
    return f

def get_gc(seq):
    gc_c=seq.count('G')+seq.count("C")
    gc_p=(gc_c/len(seq))*100
    return gc_p
dna_rec=f('gene.fna')
cds_rec=f('cds.fna')
for r in dna_rec:
    print(get_gc(r['data']))
for r in cds_rec:
    print(get_gc(r['data']))


