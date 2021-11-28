import java.awt.*;    
import javax.swing.*;    

public class NomeFrame extends JFrame {

    public NomeFrame (){
        super("Trabalho interdiciplinar");
        criarFormulario();
    }
    private void criarFormulario(){
        setLayout(new BorderLayout());

        //Ini: Titulo da guia
        JPanel painel_titulo = new JPanel();
        painel_titulo.setLayout( new FlowLayout());
    
        JLabel titulo = new JLabel("                    ");
        titulo.setFont(new Font("Verdana", Font.PLAIN,16));
    
        painel_titulo.add(titulo);
        
        //Ini: Painel de nomes
        JPanel painel_nomes= new JPanel();
        painel_nomes.setLayout( new FlowLayout());

        JLabel nomeLabel_um = new JLabel("Nome 1:");
        JTextField nomeField_um = new JTextField(22);

        JLabel nomeLabel_dois = new JLabel("Nome 2:");
        JTextField nomeField_dois = new JTextField(22);

        JLabel nomeLabel_tres = new JLabel("Nome 3:");
        JTextField nomeField_tres = new JTextField(22);

        painel_nomes.add(nomeLabel_um);
        painel_nomes.add(nomeField_um);
        painel_nomes.add(nomeLabel_dois);
        painel_nomes.add(nomeField_dois);
        painel_nomes.add(nomeLabel_tres);
        painel_nomes.add(nomeField_tres);

        //Ini: Botoes
        JPanel painel_botoes = new JPanel();
        JButton botaoSalvar = new JButton("Salvar");

        painel_botoes.add(botaoSalvar);

        //Ini: add a tela
        add(painel_titulo, BorderLayout.NORTH);
        add(painel_nomes, BorderLayout.CENTER);  
        add(painel_botoes, BorderLayout.SOUTH);      

    }
}