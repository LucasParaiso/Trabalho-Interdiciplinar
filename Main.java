import javax.swing.JFrame;

public class Main {

    public static void main(String[] args) {
        System.out.println("Hello world");
        
        NomeFrame frame = new NomeFrame();
        
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(350,220);
        frame.setVisible(true);
        
    }

}