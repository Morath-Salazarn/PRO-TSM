/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package pkg06_demoexceptions;

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
        try {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Ganzzahldivision");

            System.out.print("Dividend: ");
            int dividend = scanner.nextInt();

            System.out.print("Divisor: ");
            int divisor = scanner.nextInt();

            int quotient = dividend / divisor; // Programmabbruch, falls divisor==0
            int rest = dividend % divisor;
            System.out.println("Ergebnis: " + quotient + " Rest " + rest);

        } catch (java.lang.ArithmeticException ex) {
            System.err.println(ex.getLocalizedMessage());
        }

    }

}
