from itertools import permutations
import numpy as np
import math

codis = list(permutations(['0', '1', '00', '01','10','11'], 3))
dist = [1/3, 1/3, 1/3]

Lavs = np.zeros(len(codis))
Lav = np.zeros(3)
Kraft = np.zeros(len(codis))

entropy = 0
for k in range(3): entropy += -(dist[k]*math.log2(dist[k]))
eff = 0

cont_kr = 0
cont_lv = 0

for i in range(len(codis)):
    print(f"{i} -th code: {codis[i]}")
    for j in range(3):
        codeword = codis[i][j]

        Lav[j] = len(codeword)
        Lavs[i] += Lav[j] * dist[j]
        Kraft[i] += 2**(-Lav[j])
   
    if (Lavs[i] < 2): cont_lv += 1
    if(eff > 0.8): cont_ef += 1

    print("Kraft value", Kraft[i])
    print("Lenght: ", Lav)
    print("Average lenght", round(Lavs[i],3))
    

    if Kraft[i] > 1: print("This code does not satisfy Kraft's inequality")
    else: 
        print("This code satisfies Kraft's inequality")
        cont_kr += 1
    print("---------------------------------------------")

print("Percetage of codes that satisfy Kraft: ", cont_kr/len(codis)*100)
print("Percetage of codes that have Lav = 1,667 bits:",cont_lv)
print("Percetage of codes that have Lav = 2.0 bits:",len(codis) - cont_lv)





