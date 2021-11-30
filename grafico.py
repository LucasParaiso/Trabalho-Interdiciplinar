import tkinter
import _tkinter
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Times", "14")

        #CONTAINERS
        self.primeiroContainer = tkinter.Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = tkinter.Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer["pady"] = 5
        self.segundoContainer.pack()

        self.terceiroContainer = tkinter.Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["pady"] = 5
        self.terceiroContainer.pack()

        self.quartoContainer = tkinter.Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer["pady"] = 5
        self.quartoContainer.pack()

        self.espacamento = tkinter.Frame(master)
        self.espacamento["pady"] = 1
        self.espacamento.pack()
        self.espaco = tkinter.Label(self.espacamento, text=" ")
        self.espaco.pack()

        self.quintoContainer = tkinter.Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer["pady"] = 5
        self.quintoContainer.pack()

        self.sextoContainer = tkinter.Frame(master)
        self.sextoContainer["padx"] = 20
        self.sextoContainer["pady"] = 5
        self.sextoContainer.pack()

        self.setimoContainer = tkinter.Frame(master)
        self.setimoContainer["padx"] = 20
        self.setimoContainer["pady"] = 5
        self.setimoContainer.pack()

        self.botaoContainer = tkinter.Frame(master)
        self.botaoContainer["padx"] = 20
        self.botaoContainer["pady"] = 5
        self.botaoContainer.pack()

        #TITULO
        self.titulo = tkinter.Label(self.primeiroContainer, text="Entrada dos Nomes")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        #NOME UM
        self.nomeUmLabel = tkinter.Label(self.segundoContainer,text="Nome 1:", font=self.fontePadrao)
        self.nomeUmLabel.pack(side=tkinter.LEFT)

        self.nomeUm = tkinter.Entry(self.segundoContainer)
        self.nomeUm["width"] = 30
        self.nomeUm["font"] = self.fontePadrao
        self.nomeUm.pack(side=tkinter.LEFT)

        #NOME DOIS
        self.nomeDoisLabel = tkinter.Label(self.terceiroContainer, text="Nome 2:", font=self.fontePadrao)
        self.nomeDoisLabel.pack(side=tkinter.LEFT)

        self.nomeDois = tkinter.Entry(self.terceiroContainer)
        self.nomeDois["width"] = 30
        self.nomeDois["font"] = self.fontePadrao
        self.nomeDois.pack(side=tkinter.LEFT)

        #NOME TRES
        self.nomeTresLabel = tkinter.Label(self.quartoContainer, text="Nome 3:", font=self.fontePadrao)
        self.nomeTresLabel.pack(side=tkinter.LEFT)

        self.nomeTres = tkinter.Entry(self.quartoContainer)
        self.nomeTres["width"] = 30
        self.nomeTres["font"] = self.fontePadrao
        self.nomeTres.pack(side=tkinter.LEFT)

        #RESULTADO UM
        self.resultadoUmLabel = tkinter.Label(self.quintoContainer, text="Resultado 1:", font=self.fontePadrao)
        self.resultadoUmLabel.pack(side=tkinter.LEFT)

        self.resultadoUm = tkinter.Label(self.quintoContainer, text="", font=self.fontePadrao)
        self.resultadoUm["width"] = 29
        self.resultadoUm.pack(side=tkinter.LEFT)

        #RESULTADO DOIS
        self.resultadoDoisLabel = tkinter.Label(self.sextoContainer, text="Resultado 2:", font=self.fontePadrao)
        self.resultadoDoisLabel.pack(side=tkinter.LEFT)

        self.resultadoDois = tkinter.Label(self.sextoContainer, text="", font=self.fontePadrao)
        self.resultadoDois["width"] = 29
        self.resultadoDois.pack(side=tkinter.LEFT)

        #RESULTADO TRES
        self.resultadoTresLabel = tkinter.Label(self.setimoContainer, text="Resultado 3:", font=self.fontePadrao)
        self.resultadoTresLabel.pack(side=tkinter.LEFT)

        self.resultadoTres = tkinter.Label(self.setimoContainer, text="", font=self.fontePadrao)
        self.resultadoTres["width"] = 29
        self.resultadoTres.pack(side=tkinter.LEFT)

        #BOTAO VERIFICA NOMES
        self.botaoVerificador = tkinter.Button(self.botaoContainer)
        self.botaoVerificador["text"] = "Verificar Gênero"
        self.botaoVerificador["font"] = self.fontePadrao
        self.botaoVerificador["width"] = 20
        self.botaoVerificador.bind("<Button-1>", self.nayveBaies)
        self.botaoVerificador.pack()

    def nayveBaies(self, event):
        self.baseNomes = pd.read_csv('nomes.csv')

        self.nomes = self.baseNomes.iloc[:, 0].values
        self.genero = self.baseNomes.iloc[:, 1].values

        self.baseDados = []
        self.aux = []

        for i in self.nomes:
            self.aux.append(i[-1])
            self.aux.append(i[-2] + i[-1])
            self.baseDados.append(self.aux)
            self.aux = []

        self.baseDados = np.array(self.baseDados)

        self.labelEncoderUltimaLetra = LabelEncoder()
        self.labelEncoderDuasUltimasLetras = LabelEncoder()

        self.baseDados[:,0] = self.labelEncoderUltimaLetra.fit_transform(self.baseDados[:,0])
        self.baseDados[:,1] = self.labelEncoderDuasUltimasLetras.fit_transform(self.baseDados[:,1])

        self.naiveNomes = GaussianNB()
        self.naiveNomes.fit(self.baseDados, self.genero)

        self.verificar = [self.nomeUm.get(), self.nomeDois.get(), self.nomeTres.get()]

        self.verificaNome()
        
        if self.resultado[0] == 'M': self.resultadoUm["text"] = "Masculino"
        elif self.resultado[0] == 'F': self.resultadoUm["text"] = "Feminino"
        
        if self.resultado[1] == 'M': self.resultadoDois["text"] = "Masculino"
        elif self.resultado[1] == 'F': self.resultadoDois["text"] = "Feminino"

        if self.resultado[2] == 'M': self.resultadoTres["text"] = "Masculino"
        elif self.resultado[2] == 'F': self.resultadoTres["text"] = "Feminino"

    def verificaNome(self):
        self.nomeDados = []
        self.nomeDadosUm = 0
        self.nomeDadosDois = 0
        self.resultado = []

        for x in range(0, 3):
            for i in range(0, 1264):
                if (self.nomes[i][-1] == self.verificar[x][-1]):
                    self.nomeDadosUm = self.baseDados[i][0]
                    break

            for i in range(0, 1264):
                if (self.nomes[i][-1] == self.verificar[x][-1] and self.nomes[i][-2] == self.verificar[x][-2]):
                    self.nomeDadosDois = self.baseDados[i][1]
                    break

            self.previsao = self.naiveNomes.predict([[self.nomeDadosUm, self.nomeDadosDois], [self.nomeDadosUm, self.nomeDadosDois]])
            self.resultado.append(self.previsao[0])

root = tkinter.Tk()
Application(root)
root.mainloop()