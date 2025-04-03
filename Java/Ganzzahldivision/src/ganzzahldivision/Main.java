/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ganzzahldivision;

import java.util.Scanner;

/**
 *
 * @author maxi-leidl
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Dividend: ");
        int dividend = Integer.parseInt(scanner.nextLine());
        
        System.out.println("Divisor: ");
        int divisor = Integer.parseInt(scanner.nextLine());
        
        int quotient = 0;
        int rest = 0;
        
        try{
            quotient = dividend / divisor;
            rest = dividend % divisor;
            System.out.println("Ergebnis: " + quotient + " Rest " + rest);
        } catch(java.lang.ArithmeticException ex){
            System.err.println(ex.getLocalizedMessage());
        }
        
    }
    
}
