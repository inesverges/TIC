import itertools
import numpy as np

alphabet = ['A', 'C', 'G', 'T']
sortides = []

missatges_aux = ['AAA','CCC','GGG','TTT']
missatges = []

probabilitats = [1/2, 1/4, 1/8, 1/8]

#missatges com a seqüència de lletres sense espaiar
for i in missatges_aux:
    seq2 = ''.join(i)
    missatges.append(seq2)

for z in itertools.product(alphabet, repeat=3):
    seq = ''.join(z)
    sortides.append(seq)


#funció per calcular la probabilitat d'error del i-èssim missatge d'entrada
def peM(num, p, boolean):
    if num >= len(missatges): return

    Pe = 0  #Probabilitat error missatge m

    for y in sortides:
        probsYXm = []  #Probabilitat P(y|x_m) per a cada missatge m

        for m in missatges:
            prob = 1
            for i in range(3): #Longitud de cada missatge
                if y[i] == m[i]:
                    prob *= (1 - p)
                else:
                    prob *= p / 3
            probsYXm.append(prob)

        #Comprovem si hi ha empat probabilistic i el resolvem
        if empat(y, missatges): m_dec = resol_empat(y,missatges)
        
        else:

            m_dec = np.argmax(probsYXm) #MLD
            

        #Si pertany a la regió d'error, calculem la prob d'error
        if m_dec != num:
            Pe += probsYXm[num]

    if boolean: print("La probabilitat d'error del missatge", num, "amb p =", p, "és: ", round(Pe,4))
    return Pe


def empat(y,missatges): #Verifica missatges que tenen una coincidència

    coincidencies = []
    for m in missatges:
        numC = 0
        for i in range(3):
            if y[i] == m[i]:
                numC += 1
        coincidencies.append(numC)
    return all(c == 1 for c in coincidencies)  #Retorna tots els missatges que tenen exactament una coincidència

def resol_empat(y, missatges): #Resol l'empat
    for idx, m in enumerate(missatges): 
        if m[0] == y[0]: return idx #retorna l'index (és a dir, la primera lletra) del missatge

def PeCodi(probs,p): #Probabilitat del codi
    peTotal = 0
    for i in range(len(missatges)):
        peTotal += peM(i,p,False)*probs[i]

    print("La probabilitat total del codi amb p =", p, "és: ", round(peTotal,4))
    return peTotal

peM(2,0.2,True)
PeCodi(probabilitats,0.2)



