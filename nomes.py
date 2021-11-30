import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

baseNomes = pd.read_csv('nomes.csv')

nomes = baseNomes.iloc[:, 0].values
genero = baseNomes.iloc[:, 1].values

baseDados = []
aux = []

for i in nomes:
    aux.append(i[-1])
    aux.append(i[-2] + i[-1])
    baseDados.append(aux)
    aux = []

baseDados = np.array(baseDados)

labelEncoderUltimaLetra = LabelEncoder()
labelEncoderDuasUltimasLetras = LabelEncoder()

baseDados[:,0] = labelEncoderUltimaLetra.fit_transform(baseDados[:,0])
baseDados[:,1] = labelEncoderDuasUltimasLetras.fit_transform(baseDados[:,1])

naiveNomes = GaussianNB()
naiveNomes.fit(baseDados, genero)

def nayveBaies(nome, nomes, baseDados, naiveNomes):
    nomeDadosUm = 0
    nomeDadosDois = 0

    for i in range(0, 1264):
        if (nomes[i][-1] == nome[-1]):
            nomeDadosUm = baseDados[i][0]
            break

    for i in range(0, 1264):
        if (nomes[i][-1] == nome[-1] and nomes[i][-2] == nome[-2]):
            nomeDadosDois = baseDados[i][1]
            break

    print(nomeDadosUm)
    print(nomeDadosDois)
    previsao = naiveNomes.predict([[nomeDadosUm, nomeDadosDois], [nomeDadosUm, nomeDadosDois]])
    print(previsao)

    return previsao[0]

while(True):
    nomeUm = input('\n\nPrimeiro Nome: ')
    nomeDois = input('Segundo Nome: ')
    nomeTres = input('Terceiro Nome: ')
    verificar = [nomeUm, nomeDois, nomeTres]
    aux = []

    for i in range(0, 3):
        #print(nayveBaies('Lucas', nomes, baseDados, naiveNomes))
        aux.append(nayveBaies(verificar[i], nomes, baseDados, naiveNomes))
    
    print('\n')
    for i in range(0, 3):
        if (aux[i] == 'M'):
            print(verificar[i] + ' é Masculino')
        elif (aux[i] == 'F'):
            print(verificar[i] + ' é Feminino')

    