#!/usr/bin/python3
sek=int(input())
ch=sek//3600
mi=(sek//60)-ch*60
sek=sek%60
print(f'{ch:02d}',':',f'{mi:02d}',':',f'{sek:02d}')



