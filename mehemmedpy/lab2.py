#12
#C(n) ədədi massivinin(siyahının) tək indeksli elementlərinin hasilini hesablayan alqoritm tərtib etməli
import random
Hasil=1
C = []
for i in range(0,10):
    n = random.randint(0,200)
    C.append(n)

for x in C:
    if C.index(x)%2==1:
        Hasil*=int(x)
print(Hasil)
    