/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package wiederholung.history;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Stack;

/**
 *
 * @author maxi-leidl
 */
public class WiederholungHistory {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        try {
            // TODO code application logic here
            Path pfad = Paths.get("/home/maxi-leidl/Documents/PRO Code/PRO-TSM/Java/Wiederholung history/history.csv");
            
            for(String zeile : Files.readAllLines(pfad)){
                // Schritt 1: Zerlegen in Teilstrings
                String[] teile = zeile.split(";");

                // Schritt 2: Ausgabe mit Leerzeichen
                System.out.println(String.join(" ", teile));

                // Schritt 3: Stack benutzen, um Reihenfolge umzudrehen
                Stack<String> stack = new Stack<>();
                for (String t : teile) {
                    stack.push(t);
                }
                while (!stack.isEmpty()) {
                    
                }
            
            }
        }
        catch (IOException ex) {
            System.getLogger(WiederholungHistory.class.getName()).log(System.Logger.Level.ERROR, (String) null, ex);
        }
        
    }
    
}
