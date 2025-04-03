/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package zufallszahlen;

import java.util.Random;
import java.util.ArrayList;

/**
 *
 * @author maxi-leidl
 */
public class Zufallszahlen {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Random random = new Random(10);

        Arraylist<Integer> liste = new Arraylist<>();

        for (int i = 0; i < 1000000; i++) {
            int zufallszahl = random.nextInt(10);
            liste.add(zufallszahl);
        }

        // TODO code application logic here
    }

}
