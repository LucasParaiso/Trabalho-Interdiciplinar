from java.lang import System
from javax.swing import JFrame, JPanel, JLabel, JTextField, JButton
from java.awt import FlowLayout
from java.awt.event import ActionListener

class InterfaceGrafica(object):
    def __init__(self):
        #Frame Principal
        self.frame = JFrame('Trabalho interdiciplinar')
        self.frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.frame.setLocation(100, 100)
        self.frame.setSize(300, 200)
        self.frame.setLayout(FlowLayout())

        #Titulo
        self.titulo = JLabel('Trabalho interdiciplinar')

        #Nomes
        self.painelNomeUm = JPanel()
        self.nomeLabelUm = JLabel('Nome 1:')
        self.nomeTextFieldUm = JTextField(20)

        self.painelNomeDois = JPanel()
        self.nomeLabelDois = JLabel('Nome 2:')
        self.nomeTextFieldDois = JTextField(20)

        self.painelNomeTres = JPanel()
        self.nomeLabelTres = JLabel('Nome 3:')
        self.nomeTextFieldTres = JTextField(20)

        self.painelNomeUm.add(self.nomeLabelUm)
        self.painelNomeUm.add(self.nomeTextFieldUm)
        self.painelNomeDois.add(self.nomeLabelDois)
        self.painelNomeDois.add(self.nomeTextFieldDois)
        self.painelNomeTres.add(self.nomeLabelTres)
        self.painelNomeTres.add(self.nomeTextFieldTres)

        #Botao
        self.botaoSalvar = JButton('Verificar', actionPerformed = self.verificarNomes)
        
        #Adiciona ao Frame
        self.frame.add(self.titulo)
        self.frame.add(self.painelNomeUm)
        self.frame.add(self.painelNomeDois)
        self.frame.add(self.painelNomeTres)
        self.frame.add(self.botaoSalvar)

        self.frame.setVisible(True)
    
    def verificarNomes(self, event):
        self.nomeTextFieldUm.setText('Gustavo')
        self.nomeTextFieldDois.setText('Lucas')
        self.nomeTextFieldTres.setText('Matheus')

if __name__ == '__main__':
    InterfaceGrafica()