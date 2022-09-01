
import javax.swing.JOptionPane;

public class Excecoes {
   public static void main (String[] args){
       try {
           int num1 = Integer.parseInt(JOptionPane.showInputDialog("Primeiro número:"));
           int num2 = Integer.parseInt(JOptionPane.showInputDialog("Segundo número:"));
           int div = num1/num2;
           JOptionPane.showMessageDialog(null,"Resultado da sua divisão: " + div);
       
       } catch (ArithmeticException e) {
           JOptionPane.showMessageDialog(null,"Não é possível dividir um número por 0, tente novamente");
           
       }
   } 
}

